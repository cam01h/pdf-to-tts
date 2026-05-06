# Python learning project - PDF -> TTS

This is a little learning project I set myself. The plan is to form a pipeline that ingests PDFs via the pymupdf4llm library and chunks into individual sentences, then each sentence is passed to the Kokoro library for TTS. FFMPEG then stitches each file back together.

This project is not planned to be a catch all TTS pipeline but more as a personal project for me to learn some more python skills and take some large public documents I have to learn for my day job and turn them into a chilled audiobook a can listen to at my convenience.

## Requirements
- Python 3.11+
- FFMPEG (system install)

## Python dependencies
- pymupdf4llm
- pysbd
- kokoro
- soundfile
- numpy
