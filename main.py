import sys
from pathlib import Path
from config import UNCLEAN_MD_PATH, CLEAN_MD_PATH, TTS_OUTPUT, FINAL_OUTPUT
from pipeline.extract import extract_pdf
from pipeline.clean import clean_md
from pipeline.tts import tts_loop
from pipeline.stitch import stitch

if __name__ == "__main__":
    extract_pdf(Path(sys.argv[1]), UNCLEAN_MD_PATH)
    clean_md(UNCLEAN_MD_PATH, CLEAN_MD_PATH)
    tts_loop(CLEAN_MD_PATH, TTS_OUTPUT)
    stitch(TTS_OUTPUT, FINAL_OUTPUT)
