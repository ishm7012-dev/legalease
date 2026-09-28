from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from gemini_generator import GeminiDocumentGenerator

router = APIRouter()

class DocumentRequest(BaseModel):
    document_type: str
    parties: str
    terms: str
    dates: str

@router.post("/generate")
def generate_legal_document(request: DocumentRequest):
    try:
        gemini_generator = GeminiDocumentGenerator()
        
        # Make sure this matches the method name inside gemini_generator.py!
        response = gemini_generator.generate_document(
            request.document_type,
            request.parties,
            request.terms,
            request.dates
        )
        return {"document": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))