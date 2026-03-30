from src.pdf_processor import PDFProcessor
from skills.paper_extraction_skill import PaperExtractionSkill
from typing import Optional

class PaperAgent:
    def __init__(self):
        self.pdf_processor = PDFProcessor()
        self.extraction_skill = PaperExtractionSkill()
    
    def process_paper(self, pdf_path: str) -> Optional[str]:
        # 提取PDF文本
        print(f"[test] pdf_path is {pdf_path}")
        paper_text = self.pdf_processor.extract_text(pdf_path)
        if not paper_text:
            return None
        
        # 使用技能提取论文各部分
        extracted_sections = self.extraction_skill.extract_paper_sections(paper_text)
        return extracted_sections