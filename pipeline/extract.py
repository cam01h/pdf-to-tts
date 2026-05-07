import pymupdf4llm
from config import EXTRACTION_MARGINS


def extract_pdf(pdf_path, output_path):
    md = pymupdf4llm.to_markdown(pdf_path, margins=EXTRACTION_MARGINS)
    output_path.write_text(md)
    return
