from src.ntfy import send_notification
from src.get_env import get_env
env = get_env()

def turn_ac_f(is_turn_on: bool) -> None:
    if is_turn_on:
        send_notification(env["NTFY_KEY"], {"state": True})
        return "ok now the air conditioning is on."
    else:
        send_notification(env["NTFY_KEY"], {"state": False})
        return "ok now the air conditioning is off."
        
turn_ac_f_desc = {
    "type": "function",
    "function": {
        "name": "turn_ac_f",
        "description": "Turn the air conditioning on or off.",
        "parameters": {
            "type": "object",
            "properties": {
                "is_turn_on": {
                    "type": "boolean",
                    "description": "Whether to turn the air conditioning on."
                },
            },
            "required": ["is_turn_on"]
        },
    }
}

# exposed ###########################################################################below

tools = [
    {
        "f": turn_ac_f,
        "desc": turn_ac_f_desc
    }
]

def get_tools_desc():
    return [tool["desc"] for tool in tools]

def call_tool(tool_name: str, args: dict) -> dict:
    for tool in tools:
        if tool["desc"]["function"]["name"] == tool_name:
            return tool["f"](**args)
    raise Exception(f"Tool {tool_name} not found")