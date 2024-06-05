from openai import OpenAI

OAI_MODEL_NAME = "gpt-4o"
OR_MODEL_NAME = "openai/gpt-4o"

class Message:
    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content

    def to_dict(self):
        return {
            "role": self.role,
            "content": self.content
        }

    @staticmethod
    def from_dict(data: dict):
        return Message(data["role"], data["content"])
    
class UserMessage(Message):
    def __init__(self, content: str):
        super().__init__("user", content)

class BotMessage(Message):
    def __init__(self, content: str):
        super().__init__("bot", content)
        
class SystemMessage(Message):
    def __init__(self, content: str):
        super().__init__("system", content)

class LLM:
    client: OpenAI
    messages: list
    model_name: str
    def __init__(self, env: dict):
        self.is_openrouter = env["is_openrouter"]
        args = {
            "api_key": env["OPENROUTER_API_KEY"] if self.is_openrouter else env["OPENAI_API_KEY"]
        }
        if self.is_openrouter:
            args["base_url"] = "https://openrouter.ai/api/v1"
        self.client = OpenAI(**args)
        self.model_name = OR_MODEL_NAME if self.is_openrouter else OAI_MODEL_NAME
        self.messages = []
    
    def add_message(self, message: Message):
        self.messages.append(message.to_dict()) 
        
    def inference(self):
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=self.messages,
            temperature=0,
            stream=True
        )
        
        return response
        