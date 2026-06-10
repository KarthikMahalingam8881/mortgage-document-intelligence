import pytesseract
from pdf2image import convert_from_bytes


def extract_text_with_ocr(pdf_bytes: bytes):

    try:
        pages = convert_from_bytes(pdf_bytes)

        full_text = ""

        for image in pages:
            text = pytesseract.image_to_string(image)
            full_text += text + "\n"

        print("OCR Text Length:", len(full_text))

        return full_text

    except Exception as e:
        raise RuntimeError(
            f"OCR processing failed: {str(e)}"
        )