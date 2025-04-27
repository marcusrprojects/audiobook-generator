#!/bin/bash

# download_voices.sh
# Script to automatically fetch recommended Piper TTS voices for Audiobook Generator

set -e

echo "✨ Downloading Piper voice models..."

# Create base voices directory
mkdir -p voices/en_US/joe-medium
mkdir -p voices/en_US/libritts_r-medium
mkdir -p voices/en_GB/cori-high
mkdir -p voices/en_GB/jenny_dioco-medium

# Download Joe (American English, medium quality)
curl -L -o voices/en_US/joe-medium/en_US-joe-medium.onnx \
  https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/joe/medium/en_US-joe-medium.onnx
curl -L -o voices/en_US/joe-medium/en_US-joe-medium.onnx.json \
  https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/joe/medium/en_US-joe-medium.onnx.json

# Download LibriTTS R (American English, medium quality)
curl -L -o voices/en_US/libritts_r-medium/en_US-libritts_r-medium.onnx \
  https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/libritts_r/medium/en_US-libritts_r-medium.onnx
curl -L -o voices/en_US/libritts_r-medium/en_US-libritts_r-medium.onnx.json \
  https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/libritts_r/medium/en_US-libritts_r-medium.onnx.json

# Download Cori (British English, high quality)
curl -L -o voices/en_GB/cori-high/en_GB-cori-high.onnx \
  https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_GB/cori/high/en_GB-cori-high.onnx
curl -L -o voices/en_GB/cori-high/en_GB-cori-high.onnx.json \
  https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_GB/cori/high/en_GB-cori-high.onnx.json

# Download Jenny Dioco (British English, medium quality)
curl -L -o voices/en_GB/jenny_dioco-medium/en_GB-jenny_dioco-medium.onnx \
  https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_GB/jenny_dioco/medium/en_GB-jenny_dioco-medium.onnx
curl -L -o voices/en_GB/jenny_dioco-medium/en_GB-jenny_dioco-medium.onnx.json \
  https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_GB/jenny_dioco/medium/en_GB-jenny_dioco-medium.onnx.json
