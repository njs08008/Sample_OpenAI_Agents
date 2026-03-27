from pypdf import PdfReader
from pypdf.errors import PdfReadError, PdfStreamError

def extract_text_from_pdf(file_path: str) -> str:
    try:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text.strip()
    except (PdfReadError, PdfStreamError) as e:
        print(f"Could not read PDF {file_path}: {e}")
        return ""
