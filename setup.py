from setuptools import setup

setup(
    name="audiobook-generator",
    version="0.1.0",
    py_modules=["audiobook_generator"],
    install_requires=[
        "piper-tts",
        "piper-phonemize-cross",
        "onnxruntime",
        "numpy",
        "PyPDF2",
        "pydub",
        "num2words",
        "tqdm",
        "ebooklib",
        "html2text",
        "beautifulsoup4",
    ],
    entry_points={
        "console_scripts": [
            "audiobook-gen = audiobook_generator:main"
        ]
    },
    author="Your Name",
    description="Generate audiobooks from PDF/EPUB/TXT using Piper TTS",
    url="https://github.com/youruser/audiobook-generator",
)