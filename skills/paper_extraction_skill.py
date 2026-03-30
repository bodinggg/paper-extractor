import requests
from typing import Optional
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

class PaperExtractionSkill:
    def __init__(self):
        # 获取API密钥和基础URL
        self.api_key = os.getenv("ANTHROPIC_API_KEY")
        self.base_url = os.getenv("ANTHROPIC_BASE_URL", "https://api.anthropic.com")
        self.model = os.getenv("ANTHROPIC_MODEL", "claude-3-sonnet-20240229")
        
    
    def extract_paper_sections(self, paper_text: str) -> Optional[str]:
        try:
            # 创建提示模板
            prompt = f"""
            请从以下论文文本中提取出以下几个部分：
            
            1. 背景：论文研究的背景和动机是什么？
            2. 挑战：论文要解决的主要挑战是什么？
            3. 创新点：论文的主要创新点是什么？
            4. 方法：论文提出的方法或技术是什么？
            5. 实验：论文进行了哪些实验，得到了什么结果？
            
            请按照以下格式输出，每个部分用标题和内容组成：
            
            ## 背景
            [背景内容]
            
            ## 挑战
            [挑战内容]
            
            ## 创新点
            [创新点内容]
            
            ## 方法
            [方法内容]
            
            ## 实验
            [实验内容]
            
            论文文本：
            {paper_text}
            """
            
            # 构建请求数据
            data = {
                "model": self.model,
                "max_tokens": 2000,
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            }
            
            # 设置请求头
            headers = {
                "Content-Type": "application/json",
                "x-api-key": self.api_key,
                "anthropic-version": "2023-06-01"
            }
            
            # 发送请求
            print(f"正在调用API: {self.base_url}/v1/messages")
            print(f"使用模型: {self.model}")
            
            # 增加超时时间，因为API可能需要更长时间响应
            response = requests.post(
                f"{self.base_url}/v1/messages",
                json=data,
                headers=headers,
                timeout=60  # 增加到60秒超时
            )
            
            # 打印响应状态和内容（仅用于调试）
            print(f"API响应状态: {response.status_code}")
            
            # 检查响应状态
            response.raise_for_status()
            
            # 解析响应
            result = response.json()
            
            # 查找包含text的内容元素
            for item in result.get("content", []):
                if "text" in item:
                    return item["text"]
            
            # 如果没有找到text元素，返回None
            print("未找到包含text的响应内容")
            return None
        except requests.exceptions.HTTPError as e:
            print(f"API请求失败: {e}")
            print(f"响应内容: {response.text}")
            
            # 检查是否是模型不存在错误
            if "model_not_found" in response.text:
                
                print("1. 修改.env文件中的ANTHROPIC_MODEL配置")
                print("2. 联系API服务提供商确认支持的模型")
                print("3. 考虑使用其他API服务")
            
            return None
        except Exception as e:
            print(f"Error extracting paper sections: {e}")
            return None