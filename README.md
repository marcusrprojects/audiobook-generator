# 📖 Audiobook Generator

Turn any **PDF**, **EPUB**, or **TXT** file into a professional-quality **audiobook** using **Piper TTS**.  
Everything runs **locally** — no internet connection or server required.

---

## 🚀 Features

- 📚 Supports **PDF**, **EPUB**, and **plain text** formats
- 🗣️ Multiple **Piper TTS** voices (American and British English)
- ⏸️ Smart pauses after sentences, commas, and paragraphs
- 🛠️ Text normalization (expand numbers, abbreviations)
- 🎵 Outputs **WAV** or **MP3** files with optional metadata (title, artist)
- 💻 100% offline — no server, no data collection

---

## 🛠 Installation

1. Clone the repository:

```bash
git clone https://github.com/marcusrprojects/audiobook-generator.git
cd audiobook-generator
```

2. Install the package:

```bash
pip install .
```

Or if you prefer:

```bash
pip install -r requirements.txt
```

---

## 📥 Downloading Voice Models

This tool uses **Piper TTS models** (ONNX format) for speech synthesis.

You can download free models from [HuggingFace Piper Voices](https://huggingface.co/rhasspy/piper-voices).

Example for **Joe (American English, medium quality)**:

```bash
mkdir -p voices/en_US/joe-medium
cd voices/en_US/joe-medium
curl -L -o en_US-joe-medium.onnx \
  https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/joe/medium/en_US-joe-medium.onnx
curl -L -o en_US-joe-medium.onnx.json \
  https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/joe/medium/en_US-joe-medium.onnx.json
cd ../../../..
```

Recommended Voices:

| Voice | Path | Notes |
|:------|:-----|:------|
| **LibriTTS R (US, medium)** | `voices/en_US/libritts_r-medium/` | Neutral American narrator |
| **Joe (US, medium)** | `voices/en_US/joe-medium/` | Clear American male |
| **Cori (UK, high quality)** | `voices/en_GB/cori-high/` | High-quality British female |
| **Jenny Dioco (UK, medium)** | `voices/en_GB/jenny_dioco-medium/` | Warm British voice |

---

## 🌟 Usage

### Basic usage (interactive voice selection)

```bash
audiobook-gen input_file.pdf output_file.mp3
```

You will be prompted to select a voice model if you don't specify one.

---

### Advanced usage (specify model manually)

```bash
audiobook-gen input_file.epub output_file.wav --model voices/en_US/joe-medium/en_US-joe-medium.onnx
```

---

### Adding metadata (for MP3s)

```bash
audiobook-gen book.txt audiobook.mp3 --title "My Audiobook" --artist "Author Name"
```

---

## ⚡ Example

```bash
audiobook-gen my_book.pdf my_audiobook.mp3
```

---

## 📚 Supported Formats

- `.pdf` (scanned PDFs with selectable text)
- `.epub` (standard e-book format)
- `.txt` (plain text files)

---

## 🧐 How It Works

- Extracts and normalizes text from your document
- Splits text intelligently by sentences and commas
- Synthesizes natural-sounding speech with pauses
- Outputs ready-to-listen WAV or MP3 files

---

## 📝 Requirements

- Python 3.8 or higher
- ONNX Runtime
- Piper TTS models
- Listed in [`requirements.txt`](requirements.txt)

---

## 📦 Packaging Notes

This project is fully pip-installable.  
Later, you can bundle it into a single executable using [PyInstaller](https://pyinstaller.org/):

```bash
pip install pyinstaller
pyinstaller --onefile audiobook_generator.py
```

---

## 📜 License

MIT License — free for personal and commercial use.

---

## ✨ Future Plans

- Batch conversion
- Desktop GUI version (Tauri or Electron)
- Streaming audiobook generation
- Additional language support

---

## 📩 Contact

Open an issue on [GitHub](https://github.com/marcusrprojects/audiobook-generator/issues).

---

## 🏁 Let's turn your books into beautiful audiobooks
