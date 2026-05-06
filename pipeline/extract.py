import pymupdf4llm
from config import EXTRACTION_MARGINS


def extract_pdf(pdf_path, output_path):
    md = pymupdf4llm.to_markdown(pdf_path, EXTRACTION_MARGINS)
