from setuptools import setup
from pathlib import Path

# Read the project README for a long description
here = Path(__file__).parent
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="audiobook-generator",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Generate audiobooks from PDF/EPUB/TXT using Piper TTS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/youruser/audiobook-generator",
    py_modules=["audiobook_generator"],
    python_requires=">=3.8",
    install_requires=[
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
            "audiobook-gen = audiobook_generator:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
