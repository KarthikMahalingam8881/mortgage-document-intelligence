from fastapi import FastAPI, UploadFile, File

from app.services.pdf_parser import extract_text_from_pdf
from app.services.ocr import extract_text_with_ocr
from app.services.validator import has_sufficient_text
from app.services.llm import analyze_document as analyze_with_llm

from app.models.analysis import AnalysisResponse
from fastapi import HTTPException

import time

app = FastAPI(
    title="Mortgage Document Intelligence API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Mortgage Document Intelligence API"
    }


@app.post("/analyze")
async def analyze_document(
    file: UploadFile = File(...)
):  
    start_time = time.time()

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
        status_code=400,
        detail="Only PDF files are supported"
        )
    pdf_bytes = await file.read()

    extraction_result = extract_text_from_pdf(pdf_bytes)

    text = extraction_result["text"]
    pages = extraction_result["pages"]

    ocr_used = False

    if not has_sufficient_text(text):

        text = extract_text_with_ocr(pdf_bytes)

        ocr_used = True

    text_length = len(text)
    print("TEXT LENGTH:", len(text))
    try:
        analysis = analyze_with_llm(text)
        validated_analysis = AnalysisResponse(**analysis)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    processing_time = round(
    time.time() - start_time,
    2
    )

    return {
        "filename": file.filename,
        "processing": {
            "ocr_used": ocr_used,
            "pages": pages,
            "text_length": text_length,
            "processing_time_seconds": processing_time
        },
        "analysis": validated_analysis.model_dump()
    }