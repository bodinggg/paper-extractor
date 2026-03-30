# 论文提取系统开发文档

## 1. 系统概述

论文提取系统是一个基于Python的工具，能够从PDF格式的学术论文中自动提取背景、挑战、创新点、方法和实验等关键部分，并生成结构化的整理结果。

### 1.1 核心功能

- PDF文本提取：从PDF文件中提取文本内容
- 论文结构分析：识别并提取论文的关键部分
- 结构化输出：按照预设格式输出提取结果
- 命令行界面：提供便捷的命令行操作接口

### 1.2 技术栈

- **Python 3.11+**：主要开发语言
- **PyPDF2**：PDF文本提取库
- **LangChain**：LLM应用开发框架
- **Anthropic API**：文本分析和提取引擎
- **Typer**：命令行界面开发
- **Pydantic**：数据验证和序列化

## 2. 系统架构

### 2.1 模块划分

系统采用模块化设计，主要包含以下模块：

1. **PDF处理模块**：负责从PDF文件中提取文本内容
2. **技能模块**：负责使用LLM分析文本并提取关键部分
3. **Agent模块**：协调各模块工作，提供统一接口
4. **命令行界面**：提供用户交互入口

### 2.2 模块关系图

```
+------------------+
| 命令行界面 (main.py) |
+------------------+
          |
          v
+------------------+
|   Agent模块      |
| (paper_agent.py) |
+------------------+
          |
          +---------------------+
          |                     |
          v                     v
+------------------+    +------------------+
| PDF处理模块      |    | 技能模块         |
| (pdf_processor.py)|  | (paper_extraction_skill.py) |
+------------------+    +------------------+
```

## 3. 模块详细说明

### 3.1 PDF处理模块 (`src/pdf_processor.py`)

#### 3.1.1 功能描述

负责从PDF文件中提取文本内容，是整个系统的数据输入层。

#### 3.1.2 核心类与方法

```python
class PDFProcessor:
    @staticmethod
    def extract_text(pdf_path: str) -> Optional[str]:
        # 从PDF文件中提取文本
        # 参数：pdf_path - PDF文件路径
        # 返回：提取的文本内容，失败返回None
```

#### 3.1.3 依赖关系

- **PyPDF2**：用于PDF文本提取

### 3.2 技能模块 (`skills/paper_extraction_skill.py`)

#### 3.2.1 功能描述

使用OpenAI API分析论文文本，提取背景、挑战、创新点、方法和实验等关键部分。

#### 3.2.2 核心类与方法

```python
class PaperExtractionSkill:
    def __init__(self):
        # 初始化LLM和提示模板
    
    def extract_paper_sections(self, paper_text: str) -> Optional[str]:
        # 使用LLM提取论文各部分
        # 参数：paper_text - 论文文本内容
        # 返回：提取的结构化内容，失败返回None
```

#### 3.2.3 依赖关系

- **LangChain**：LLM应用开发框架
- **OpenAI API**：文本分析引擎
- **python-dotenv**：环境变量管理

### 3.3 Agent模块 (`agents/paper_agent.py`)

#### 3.3.1 功能描述

协调PDF处理模块和技能模块，提供统一的接口供上层调用。

#### 3.3.2 核心类与方法

```python
class PaperAgent:
    def __init__(self):
        # 初始化PDF处理器和提取技能
    
    def process_paper(self, pdf_path: str) -> Optional[str]:
        # 处理PDF论文
        # 参数：pdf_path - PDF文件路径
        # 返回：提取的结构化内容，失败返回None
```

#### 3.3.3 依赖关系

- **PDF处理模块**：提供文本提取功能
- **技能模块**：提供论文分析功能

### 3.4 命令行界面 (`main.py`)

#### 3.4.1 功能描述

提供命令行接口，方便用户使用系统。

#### 3.4.2 核心函数

```python
@app.command()
def extract_paper(pdf_path: str, output_path: str = None):
    # 从PDF论文中提取关键部分
    # 参数：
    #   pdf_path - PDF文件路径
    #   output_path - 输出文件路径（可选）
```

#### 3.4.3 依赖关系

- **Typer**：命令行界面开发
- **Agent模块**：提供核心功能

## 4. 配置管理

### 4.1 环境变量

系统使用`.env`文件管理环境变量，主要配置项：

- `ANTHROPIC_API_KEY`：Anthropic API密钥
- `ANTHROPIC_BASE_URL`：Anthropic API基础URL（可选，默认值：https://api.anthropic.com/v1）

### 4.2 依赖管理

项目使用`requirements.txt`文件管理依赖，主要依赖：

```
PyPDF2==2.12.1
langchain==0.2.14
langchain-anthropic==0.1.20
anthropic==0.32.0
python-dotenv==1.0.1
pydantic==2.12.5
typer==0.24.1
```

## 5. 开发流程

### 5.1 安装开发环境

1. 克隆项目：
   ```bash
   git clone <repository-url>
   cd paper-extractor
   ```

2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

3. 配置环境变量：
   ```bash
   cp .env.example .env
   # 编辑.env文件，填入OpenAI API密钥
   ```

### 5.2 代码规范

- 使用PEP 8代码规范
- 使用类型提示
- 编写清晰的文档字符串
- 保持代码模块化和可维护性

### 5.3 测试流程

1. 运行单元测试：
   ```bash
   python tests/test_paper_extraction.py
   ```

2. 集成测试：
   ```bash
   python main.py extract-paper <test-pdf-path>
   ```

### 5.4 版本管理

- 使用Git进行版本控制
- 遵循语义化版本规范
- 提交前运行测试确保代码质量

## 6. 扩展指南

### 6.1 添加新功能

1. **添加新模块**：在相应目录下创建新的Python文件
2. **更新依赖**：修改`requirements.txt`添加新依赖
3. **更新文档**：更新README.md和开发文档
4. **添加测试**：在tests目录下添加测试用例

### 6.2 支持新的提取类型

1. 修改`skills/paper_extraction_skill.py`中的提示模板
2. 更新输出格式
3. 更新相关文档

### 6.3 替换LLM引擎

1. 修改`skills/paper_extraction_skill.py`中的LLM初始化代码
2. 更新依赖（如果需要）
3. 更新配置文件

## 7. 故障排除

### 7.1 常见问题

1. **PDF提取失败**：
   - 检查PDF文件是否可访问
   - 检查PDF文件是否为文本格式（非扫描件）
   - 检查PyPDF2版本是否兼容

2. **API调用失败**：
   - 检查OpenAI API密钥是否正确
   - 检查网络连接
   - 检查API调用频率是否超过限制

3. **依赖冲突**：
   - 使用`pip install --force-reinstall`重新安装依赖
   - 检查Python版本是否符合要求

### 7.2 日志记录

系统目前使用简单的print语句记录错误信息，后续可扩展为使用专业的日志库（如logging）。

## 8. 未来规划

- [ ] 添加更强大的PDF解析库（如pdfplumber）
- [ ] 支持更多论文格式（如Word、HTML）
- [ ] 添加图形界面
- [ ] 支持批量处理
- [ ] 集成更多LLM模型
- [ ] 添加更详细的错误处理和日志记录
- [ ] 支持自定义提取模板
- [ ] 添加结果导出功能（如JSON、Excel）

## 9. 贡献指南

欢迎贡献代码和提出建议！请遵循以下流程：

1. Fork项目
2. 创建功能分支
3. 提交更改
4. 运行测试确保代码质量
5. 提交Pull Request

## 10. 联系方式

如有问题或建议，请联系项目维护者。