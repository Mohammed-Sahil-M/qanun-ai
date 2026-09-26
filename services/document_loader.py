from pathlib import Path
from pypdf import PdfReader

def load_pdf_text(file_path: str) -> str:
    """
    Extracts raw text page-by-page from a PDF document.
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"PDF file not found at: {file_path}")
        
    reader = PdfReader(path)
    extracted_text = []
    
    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text()
        if text:
            extracted_text.append(text)
            
    return "\n\n".join(extracted_text)
