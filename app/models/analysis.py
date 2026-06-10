from pydantic import BaseModel


class AnalysisResponse(BaseModel):
    document_type: str
    confidence: float
    extracted_data: dict
    financial_health: str
    strengths: list[str]
    concerns: list[str]
    missing_information: list[str]
    mortgage_assessment: str
    executive_summary: str