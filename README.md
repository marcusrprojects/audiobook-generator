# 📖 Audiobook Generator

[![Latest Release](https://img.shields.io/github/v/release/marcusrprojects/audiobook-generator?label=release)](https://github.com/marcusrprojects/audiobook-generator/releases)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)

Turn any **PDF**, **EPUB**, or **TXT** file into an **audiobook** using **Piper TTS**.  
Everything runs **locally** — no internet connection or server required.

---

## 🚀 Features

- 📚 Supports **PDF**, **EPUB**, and **plain text** formats
- 🗣️ Multiple **Piper TTS** voices (American and British English)
- ⏸️ Smart pauses after sentences, commas, and paragraphs
- 🛠️ Text normalization (expand numbers, abbreviations)
- 🎵 Outputs standard **WAV** or **MP3** files
- 🏷️ Add metadata (title, artist) to MP3 files
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

5. **Install the `audiobook-generator` package**:
    *This step makes the `audiobook-gen` command available.*

    ```bash
    pip install .
    ```

6. **Download voice models**:

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

## 🌟 Usage (After Installation via `pip install .`)

Ensure your virtual environment is active (`source .venv/bin/activate` or `.venv\Scripts\activate`). You can then use the audiobook-gen command:

```bash
audiobook-gen input_file.pdf output_file.mp3
```

By default, the **LibriTTS R (US, medium)** voice is used. To specify a different model:

```bash
audiobook-gen input_file.epub output_file.wav \
  --model voices/en_GB/cori-high/en_GB-cori-high.onnx
```

Specify input format (EPUB) and output format (WAV):

```bash
audiobook-gen path/to/novel.epub final_audio.wav
```

Add metadata (MP3 only):

```bash
audiobook-gen book.txt audiobook.mp3 \
  --title "My Audiobook" --artist "Author Name"
```

List available bundled voice models:
(Lists voices defined in the script's AVAILABLE_VOICES list)

```bash
audiobook-gen --list-models
```

Show help message with all options:

```bash
audiobook-gen --help
```

---

## 📚 Supported Formats

- `.pdf` (scanned PDFs with selectable text)
- `.epub` (standard e-book format)
- `.txt` (plain text files, UTF-8 encoding preferred)

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

## 📦 Creating a Standalone Executable (Optional Alternative)

If you want to distribute this tool to users who might not have Python installed, you can bundle it into a single executable file using [PyInstaller](https://pyinstaller.org/). This is typically done by the developer for distribution.

**Steps to Create the Executable:**

1. Make sure you have followed the Installation steps 1-4 (you need the dependencies installed).
2. Install PyInstaller in your virtual environment:

```bash
pip install pyinstaller
```

3. Run PyInstaller from the project's root directory (`audiobook-generator/`):

```bash
pyinstaller --onefile audiobook_generator.py
```

*This process can take a significant amount of time and requires substantial disk space. It analyzes dependencies and bundles everything. The final executable will be placed inside a new `dist` folder.*

**Running the Standalone Executable:**

Once built, the executable in the `dist` folder can be run directly without needing Python or the virtual environment.

```bash
# Example on macOS/Linux:
cd dist
./audiobook_generator ../path/to/book.pdf output.mp3 --model ../voices/en_US/joe-medium/en_US-joe-medium.onnx

# Example on Windows:
cd dist
.\audiobook_generator.exe ..\path\to\book.pdf output.mp3 --model ..\voices\en_US\joe-medium\en_US-joe-medium.onnx
```

*Note: Paths to input files and models are relative to where you run the command.*

---

## 📦 Packaging Notes

This project is fully pip-installable.

```bash
pip install pyinstaller
pyinstaller --onefile audiobook_generator.py
```

---

## ✨ Future Plans

- Batch conversion
- Desktop GUI version (Tauri or Electron)
- Additional language support

---

## 📩 Contact

Open an issue on [GitHub](https://github.com/marcusrprojects/audiobook-generator/issues).

---

## 🏁 Let's turn your books into audiobooks
