# Mortgage Document Intelligence System

## Overview

Mortgage teams often review financial documents manually to assess borrower readiness.

This project automates document understanding by combining PDF extraction, OCR, and AI-powered analysis to generate mortgage-focused insights from uploaded documents.

---
## Demo

Input:
- Credit Reports
- Property Appraisals
- Scanned Mortgage Documents

Output:
- Document Classification
- Key Information Extraction
- Financial Assessment
- Strengths & Risks
- Missing Information
- Executive Summary

Examples are available in the `/examples` folder.
---
## Screenshots

### Swagger UI

![Swagger UI](https://github.com/KarthikMahalingam8881/mortgage-document-intelligence/blob/main/screenshots/Screenshot%201.png)

### Sample Response

![Sample Response](https://github.com/KarthikMahalingam8881/mortgage-document-intelligence/blob/main/screenshots/Screenshot%206.png)

---

## Problem Statement

The goal is not simply to parse PDFs.

The goal is to understand mortgage-related documents and produce actionable insights regarding financial health, strengths, concerns, and missing information.

---

## Architecture

PDF Upload
↓
PyMuPDF Extraction
↓
Text Available?
↓
Yes → Continue
No → OCR (Tesseract)
↓
Gemini 2.5 Flash Analysis
↓
Pydantic Validation
↓
Structured JSON Response

---

## Tech Stack

Backend:
- FastAPI

PDF Processing:
- PyMuPDF

OCR:
- Tesseract
- pdf2image
- Poppler

AI:
- Gemini 2.5 Flash

Validation:
- Pydantic

Containerization:
- Docker

---

## API Endpoint

POST /analyze

Accepts:
- PDF file

Returns:
- Document classification
- Extracted information
- Financial assessment
- Risks and concerns
- Executive summary

---

## Sample Response

{
  "filename": "Appraisal.pdf",
  "processing": {
    "ocr_used": false,
    "pages": 2
  },
  "analysis": {
    "document_type": "Property Appraisal Report",
    "confidence": 0.98,
    "financial_health": "N/A",
    "strengths": [
      "Strong appraised value",
      "Recent renovations"
    ],
    "concerns": [],
    "mortgage_assessment": "Strong collateral asset"
  }
}

Full outputs can be found in the examples folder.
---

## Running with Docker

docker build -t mortgage-ai .

docker run -p 8000:8000 \
-e GEMINI_API_KEY=YOUR_KEY \
mortgage-ai

