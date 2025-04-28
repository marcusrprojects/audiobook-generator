#!/usr/bin/env python3
"""
audiobook_generator.py

Generate a natural-sounding audiobook from PDF, EPUB, or TXT using Piper TTS.
"""

__version__ = "0.1.0"

import sys
import re
import wave
import logging
from argparse import ArgumentParser, ArgumentTypeError
from pathlib import Path
from typing import List, Optional, Dict, Tuple, TypedDict

from num2words import num2words
from piper.voice import PiperVoice
from PyPDF2 import PdfReader
from pydub import AudioSegment
from tqdm import tqdm


class Fragment(TypedDict):
    text: str
    end_sentence: bool
    end_paragraph: bool


# --------------------- Configuration ---------------------
DEFAULT_MODEL = Path('voices/en_US/libritts_r-medium/en_US-libritts_r-medium.onnx')
AVAILABLE_VOICES: List[Tuple[str, Path]] = [
    ('LibriTTS R (American, medium)', Path('voices/en_US/libritts_r-medium/en_US-libritts_r-medium.onnx')),
    ('Joe (American, medium)',        Path('voices/en_US/joe-medium/en_US-joe-medium.onnx')),
    ('Cori (British, high quality)',  Path('voices/en_GB/cori-high/en_GB-cori-high.onnx')),
    ('Jenny Dioco (British, medium)', Path('voices/en_GB/jenny_dioco-medium/en_GB-jenny_dioco-medium.onnx')),
]

# Silence durations (ms)
PAUSE_COMMA_MS = 200   # pause after commas
PAUSE_SENT_MS  = 500   # pause after sentences
PAUSE_PARA_MS  = 1000  # pause between paragraphs

# Temporary WAV file (overwritten per fragment)
TEMP_WAV = Path('_temp.wav')


# --------------------- Utility Functions ---------------------

def normalize_text(text: str) -> str:
    """
    Expand numbers, common abbreviations, and fix hyphen line-breaks.
    """
    def num_repl(match: re.Match) -> str:
        return num2words(int(match.group(0)))

    text = re.sub(r'\b\d+\b', num_repl, text)
    abbr_map = {'Dr.': 'Doctor', 'Mr.': 'Mister', 'etc.': 'etcetera'}
    for abbr, full in abbr_map.items():
        text = text.replace(abbr, full)
    return re.sub(r'-\s*\n', '', text)


def existing_file(path: str) -> Path:
    """
    Argparse type: validate that a given file exists.
    """
    p = Path(path)
    if not p.is_file():
        raise ArgumentTypeError(f"File not found: {path}")
    return p


def load_paragraphs(path: Path) -> List[str]:
    """
    Read PDF, EPUB, or TXT and split into paragraphs (double-newline).
    """
    ext = path.suffix.lower()
    if ext == '.pdf':
        reader = PdfReader(path)
        raw = '\n'.join(page.extract_text() or '' for page in reader.pages)
    elif ext == '.epub':
        from ebooklib import epub
        from html2text import html2text

        book = epub.read_epub(str(path))
        parts: List[str] = []
        for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
            html = item.get_content().decode('utf8')
            parts.append(html2text(html))
        raw = '\n\n'.join(parts)
    else:
        raw = path.read_text(encoding='utf8')

    raw = re.sub(r'\r\n?', '\n', raw)
    return [p.strip() for p in raw.split('\n\n') if p.strip()]


# --------------------- Core Logic ---------------------

def synthesize_fragments(
    paragraphs: List[str],
    model_path: Path,
    output_path: Path,
    metadata: Optional[Dict[str, str]] = None
) -> None:
    """
    Synthesize text fragments into an audiobook with natural pauses
    and a smooth tqdm progress bar.
    """
    logging.info("🔄 Loading Piper TTS model...")
    voice = PiperVoice.load(str(model_path))
    sr = voice.config.sample_rate

    fragments: List[Fragment] = []
    for para in paragraphs:
        norm = normalize_text(para)
        sentences = re.split(r'(?<=[.?!])\s+', norm)
        for si, sent in enumerate(sentences):
            sent = sent.strip()
            if not sent:
                continue
            core = sent.rstrip('.?!')
            parts = [p.strip() for p in core.split(',') if p.strip()]
            for pi, part in enumerate(parts):
                fragments.append({
                    'text': part,
                    'end_sentence': (pi == len(parts)-1),
                    'end_paragraph': (si == len(sentences)-1 and pi == len(parts)-1)
                })

    if not fragments:
        logging.error("No text fragments found to synthesize.")
        sys.exit(1)

    # Pre-generate silence
    short_pause = AudioSegment.silent(PAUSE_COMMA_MS)
    sent_pause  = AudioSegment.silent(PAUSE_SENT_MS)
    para_pause  = AudioSegment.silent(PAUSE_PARA_MS)

    audiobook = AudioSegment.empty()
    for frag in tqdm(fragments, desc="Synthesizing", unit="frag"):
        with wave.open(str(TEMP_WAV), 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(sr)
            voice.synthesize(
                frag['text'], wf,
                length_scale=1.0,
                noise_scale=0.6,
                noise_w=0.8,
                sentence_silence=0.0
            )
        audiobook += AudioSegment.from_wav(str(TEMP_WAV))

        if not frag['end_sentence']:
            audiobook += short_pause
        else:
            audiobook += sent_pause
            if frag['end_paragraph']:
                audiobook += para_pause

    if TEMP_WAV.exists():
        TEMP_WAV.unlink()

    audiobook = audiobook.normalize().fade_in(200).fade_out(200)
    ext = output_path.suffix.lower()
    if ext == '.mp3':
        audiobook.export(str(output_path), format='mp3', tags=metadata or {})
    else:
        audiobook.export(str(output_path), format='wav')


def list_models() -> None:
    """Print bundled voice model names and paths."""
    for name, path in AVAILABLE_VOICES:
        logging.info(f"{name}: {path}")


def main() -> None:
    logging.basicConfig(format='%(message)s', level=logging.INFO)
    parser = ArgumentParser(
        description='Generate an audiobook from PDF/EPUB/TXT via Piper TTS'
    )
    parser.add_argument(
        '--version', action='version', version=__version__,
        help='Show program version and exit'
    )
    parser.add_argument(
        'input', type=existing_file,
        help='Path to input file (PDF, EPUB, TXT)'
    )
    parser.add_argument(
        'output', type=Path,
        help='Path to output audio file (.wav or .mp3)'
    )
    parser.add_argument(
        '-m', '--model', type=existing_file,
        default=DEFAULT_MODEL,
        help='Path to Piper ONNX model file'
    )
    parser.add_argument(
        '--list-models', action='store_true',
        help='List available voice models and exit'
    )
    parser.add_argument('--title', help='Title metadata for MP3')
    parser.add_argument('--artist', help='Artist metadata for MP3')

    args = parser.parse_args()

    if args.list_models:
        list_models()
        sys.exit(0)

    paragraphs = load_paragraphs(args.input)
    if not paragraphs:
        logging.error('Error: No text extracted from input.')
        sys.exit(1)

    metadata: Dict[str, str] = {}
    if args.title:
        metadata['title'] = args.title
    if args.artist:
        metadata['artist'] = args.artist

    synthesize_fragments(
        paragraphs,
        args.model,
        args.output,
        metadata or None
    )
    logging.info(f'Audiobook written to {args.output}')


if __name__ == '__main__':
    main()
