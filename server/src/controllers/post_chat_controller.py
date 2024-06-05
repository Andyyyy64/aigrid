from src.get_env import get_env
from src.llm import LLM, UserMessage
from flask import Response
env = get_env()

def post_chat_controller(msg: str):
    llm = LLM(env)
    llm.add_message(UserMessage(msg))
    stream = llm.inference()
    def generate():
        responses = []
        for item in stream:
            yield item.choices[0].delta.content

        
    return Response(generate(), content_type="text/event-stream"), 200
