from src.get_env import get_env
from src.llm import LLM, UserMessage, SystemMessage, ToolCall 
from src.tools import call_tool
from flask import Response
import json
from typing import Iterator
env = get_env()

PROMPT = f"""You are home assistant girl called 'aigrid'. Your answer is always veru very short as possible."""
MAX_FC = 2;

def post_chat_controller(msg: str):
    llm = LLM(env)
    llm.add_message(SystemMessage(PROMPT))
    llm.add_message(UserMessage(msg))
    resp_text = ""
    tmf = 0
    for i in range(8):
        resp = llm.inference()
        print("*"*810)
        print(resp)
        choice = resp.choices[0]
        finish_reason = choice.finish_reason
        if finish_reason == "stop":
            resp_text = choice.message.content
            break
        elif finish_reason == "tool_calls":
            if tmf>=MAX_FC:
                resp_text = "Error: too many function calls."
                break
            tmf += 1
            for tool_call in choice.message.tool_calls:
                name = tool_call.function.name
                args = json.loads(tool_call.function.arguments)
                print(f"Calling tool {name} with args {args}")
                tool_resp = call_tool(name, args)
                llm.add_message(ToolCall(name, tool_resp))
        else:
            # error
            resp_text = f"Error: {str(resp)}"
            break
    
    print("*"*810)
    print(llm.messages)
    return Response(resp_text, mimetype="application/json"), 200
