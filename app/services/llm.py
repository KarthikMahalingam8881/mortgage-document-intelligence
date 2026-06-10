import json
import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")
# print("GEMINI KEY FOUND:", api_key is not None)

def analyze_document(document_text: str):

    prompt = f"""
You are an expert mortgage document analyst.

Return ONLY valid JSON.

{{
  "document_type":"",
  "confidence":0.0,
  "extracted_data":{{}},
  "financial_health":"",
  "strengths":[],
  "concerns":[],
  "missing_information":[],
  "mortgage_assessment":"",
  "executive_summary":""
}}

Document:

{document_text[:5000]}
"""

    response = model.generate_content(prompt)

    text = response.text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(text)

    except json.JSONDecodeError:
        raise ValueError(
        "Gemini returned invalid JSON"
        )