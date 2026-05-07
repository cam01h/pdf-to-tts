import pymupdf4llm


def extract_pdf(pdf_path, output_path):
    md = pymupdf4llm.to_markdown(pdf_path, header=False, footer=False)
    output_path.write_text(md)
    return
