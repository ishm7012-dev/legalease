import os
from google import genai

class GeminiDocumentGenerator:
    def __init__(self):
        # Explicitly pull the API key from environment variables
        api_key = "AQ.Ab8RN6JWUaZ_C2HjIqmmQIxZmVuA7WGq031pWzPyxrxBqUK0bQ"

        
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable is missing!")
            
        # Initialize the new google-genai client with the key
        self.client = genai.Client(api_key=api_key)
        self.model_name = "gemini-3.8-flash"  # or gemini-1.5-flash

    def generate_document(self, document_type, parties, terms, dates):
        prompt = (
            f"Generate a comprehensive legal document titled '{document_type}'\n"
            f"Involved parties: {parties}\n"
            f"Effective Date: {dates}\n"
            f"Terms and conditions: {terms}\n"
            f"Ensure formal legal structure with multiple sections and legal clauses."
        )
        
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt,
        )
        return response.text