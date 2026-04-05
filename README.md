# Paper Extractor

一个基于Python的论文提取系统，可以从PDF格式的学术论文中自动提取背景、挑战、创新点、方法和实验等关键部分，并生成结构化的整理结果。

## 功能特点

- 📄 从PDF文件中提取文本内容（支持pdfplumber和PyPDF2作为备选解析器）
- 🤖 使用Anthropic兼容的API提取论文关键部分：背景、挑战、创新点、方法和实验
- 🖥️ 提供简洁的命令行界面，方便使用
- 🏗️ 模块化设计，易于扩展和维护
- 🔧 支持自定义API端点和模型配置
- ⚡ 完善的错误处理和诊断信息

## 安装步骤

1. 克隆项目到本地：
```bash
git clone https://github.com/your-username/paper-extractor.git
cd paper-extractor
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 配置环境变量：
```bash
cp .env.example .env
# 编辑.env文件，填入你的API密钥和配置
```

## 使用方法

### 命令行使用

```bash
python main.py <pdf-file-path> --output-path <output-file-path>
```

示例：
```bash
python main.py paper.pdf --output-path result.md
```

### 作为模块使用

```python
from agents.paper_agent import PaperAgent

agent = PaperAgent()
result = agent.process_paper("paper.pdf")
print(result)
```

## 项目结构

```
paper-extractor/
├── src/                 # 核心功能模块
│   ├── __init__.py
│   └── pdf_processor.py # PDF文本提取（支持多种解析器）
├── skills/              # 技能模块
│   ├── __init__.py
│   └── paper_extraction_skill.py # 论文提取技能
├── agents/              # Agent模块
│   ├── __init__.py
│   └── paper_agent.py   # 论文处理Agent
├── data/                # 数据存储目录
├── tests/               # 测试目录
├── main.py              # 主程序入口
├── requirements.txt     # 依赖列表
├── .env.example         # 环境变量示例
├── .env                 # 实际环境变量
├── DEVELOPMENT.md       # 开发文档
└── LICENSE              # 开源许可证
```

## 技术栈

- Python 3.11+
- pdfplumber：主要PDF文本提取工具
- PyPDF2：备选PDF文本提取工具
- requests：API调用
- Typer：命令行界面开发
- python-dotenv：环境变量管理

## API配置

系统支持与Anthropic API兼容的服务提供商：

- **通用地址**：`https://newapi.hizui.cn/v1/messages`
- **认证字段**：`ANTHROPIC_API_KEY`
- **接口协议**：`anthropic-messages`

支持配置不同的模型，如：
- `MiniMax-M2.7`
- `claude-3-sonnet-20240229`
- 其他兼容Anthropic API的模型

## 注意事项

- 请确保你已经拥有有效的API密钥
- 系统需要网络连接才能调用API
- 对于大型PDF文件，处理时间可能会较长
- 部分加密或扫描的PDF文件可能无法正确提取文本

## 贡献

欢迎提交Issue和Pull Request！

## 许可证

MIT License
