import typer
from agents.paper_agent import PaperAgent
import os

app = typer.Typer()

@app.command()
def extract_paper(pdf_path: str, output_path: str = None):
    """
    从PDF论文中提取背景、挑战、创新点、方法和实验部分
    """
    # 检查PDF文件是否存在
    if not os.path.exists(pdf_path):
        typer.echo(f"错误：文件 {pdf_path} 不存在")
        return
    
    # 创建Agent实例
    agent = PaperAgent()
    
    # 处理论文
    typer.echo("正在处理论文...")
    result = agent.process_paper(pdf_path)
    
    if result:
        # 如果指定了输出路径，将结果写入文件
        if output_path:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(result)
            typer.echo(f"结果已保存到 {output_path}")
        else:
            # 否则直接打印结果
            typer.echo(result)
    else:
        typer.echo("处理论文失败")

if __name__ == "__main__":
    app()