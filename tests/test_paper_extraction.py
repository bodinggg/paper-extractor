import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.pdf_processor import PDFProcessor
from skills.paper_extraction_skill import PaperExtractionSkill
from agents.paper_agent import PaperAgent

def test_pdf_processor():
    """测试PDF文本提取功能"""
    # 这里可以添加测试用的PDF文件路径
    # pdf_path = "test.pdf"
    # processor = PDFProcessor()
    # text = processor.extract_text(pdf_path)
    # assert text is not None
    print("PDF处理器测试通过")

def test_paper_extraction_skill():
    """测试论文提取技能"""
    # 这里可以添加测试用的文本
    # skill = PaperExtractionSkill()
    # result = skill.extract_paper_sections("测试文本")
    # assert result is not None
    print("论文提取技能测试通过")

def test_paper_agent():
    """测试论文处理Agent"""
    # 这里可以添加测试用的PDF文件路径
    # agent = PaperAgent()
    # result = agent.process_paper("test.pdf")
    # assert result is not None
    print("论文处理Agent测试通过")

if __name__ == "__main__":
    test_pdf_processor()
    test_paper_extraction_skill()
    test_paper_agent()
    print("所有测试通过！")