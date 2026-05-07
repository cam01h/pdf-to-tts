import sys
from pathlib import Path
from config import UNCLEAN_MD_PATH
from pipeline.extract import extract_pdf

if __name__ == "__main__":
    print("extracting pdf...")
    extract_pdf(Path(sys.argv[1]), UNCLEAN_MD_PATH)
    print("pdf extracted")
