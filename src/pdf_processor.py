import pdfplumber
from typing import Optional

class PDFProcessor:
    @staticmethod
    def extract_text(pdf_path: str) -> Optional[str]:
        try:
            # 首先尝试使用pdfplumber
            with pdfplumber.open(pdf_path) as pdf:
                text = []
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text.append(page_text)
                return "\n".join(text)
        except Exception as e:
            print(f"pdfplumber error: {e}")
            # 如果pdfplumber失败，尝试使用PyPDF2作为备选
            try:
                from PyPDF2 import PdfReader
                reader = PdfReader(pdf_path)
                text = []
                for page in reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text.append(page_text)
                return "\n".join(text)
            except Exception as e2:
                print(f"PyPDF2 error: {e2}")
                return None