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

Follow these steps to set up the project and its dependencies.

1. **Clone the repository**:

    ```bash
    git clone https://github.com/marcusrprojects/audiobook-generator.git
    cd audiobook-generator
    ```

2. **Create and activate a virtual environment** (recommended):

    ```bash
    # macOS/Linux
    python3 -m venv .venv
    source .venv/bin/activate

    # Windows (PowerShell)
    .venv\Scripts\Activate.ps1
    ```

3. **Install Piper TTS packages** (manual install to satisfy dependencies):

    ```bash
    pip install piper-tts --no-deps
    pip install piper-phonemize-cross
    ```

4. **Install the remaining dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

5. **Download voice models**:

    ```bash
    bash download_voices.sh
    ```

> **Note:** `requirements.txt` includes all non-Piper dependencies. The two Piper packages must be installed manually due to naming differences.

---

## 📥 Downloading Voice Models

This tool uses **Piper TTS models** (ONNX format) for speech synthesis.

You can download free voice models from [HuggingFace Piper Voices](https://huggingface.co/rhasspy/piper-voices).

### Easy method (recommended)

Run the included script:

```bash
bash download_voices.sh
```

### Manual method (example for Joe)

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

| Voice                          | Path                                              | Notes                           |
|:-------------------------------|:--------------------------------------------------|:--------------------------------|
| **LibriTTS R (US, medium)**    | `voices/en_US/libritts_r-medium/`                 | Neutral American narrator       |
| **Joe (US, medium)**           | `voices/en_US/joe-medium/`                        | Clear American male             |
| **Cori (UK, high quality)**    | `voices/en_GB/cori-high/`                         | High-quality British female     |
| **Jenny Dioco (UK, medium)**   | `voices/en_GB/jenny_dioco-medium/`                | Warm British voice              |

---

## 🌟 Usage

After installation, you can generate an audiobook with:

```bash
audiobook-gen input_file.pdf output_file.mp3
```

By default, the **LibriTTS R (US, medium)** voice is used. To specify a different model:

```bash
audiobook-gen input_file.epub output_file.wav \
  --model voices/en_GB/cori-high/en_GB-cori-high.onnx
```

Add metadata (MP3 only):

```bash
audiobook-gen book.txt audiobook.mp3 \
  --title "My Audiobook" --artist "Author Name"
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
- Listed in [`requirements.txt`](requirements.txt) (non-Piper dependencies)
- Manual install for `piper-tts` and `piper-phonemize-cross`

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
- Additional language support

---

## 📩 Contact

Open an issue on [GitHub](https://github.com/marcusrprojects/audiobook-generator/issues).

---

## 🏁 Let's turn your books into beautiful audiobooks
