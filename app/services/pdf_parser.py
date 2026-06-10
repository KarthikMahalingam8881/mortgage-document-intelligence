import fitz


def extract_text_from_pdf(pdf_bytes: bytes):
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")

    text = ""
    page_count = len(doc)

    for page in doc:
        text += page.get_text()

    return {
        "text": text,
        "pages": page_count,
        "text_length": len(text)
    }