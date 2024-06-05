from dotenv import load_dotenv
import os

def get_env() -> dict:
    load_dotenv(override=False)
    NTFY_KEY = os.getenv("NTFY_KEY", "");
    if NTFY_KEY == "":
        raise Exception("NTFY_KEY is not set")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "");
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "");
    if OPENAI_API_KEY == "" and OPENROUTER_API_KEY == "":
        raise Exception("OPENAI_API_KEY and OPENROUTER_API_KEY is not set, please set at least one")
    if OPENAI_API_KEY != "" and OPENROUTER_API_KEY != "":
        raise Exception("OPENAI_API_KEY and OPENROUTER_API_KEY is set, please set only one")
    is_openrouter = OPENAI_API_KEY == ""
    
    return {
        "NTFY_KEY": NTFY_KEY,
        "OPENAI_API_KEY": OPENAI_API_KEY,
        "OPENROUTER_API_KEY": OPENROUTER_API_KEY,
        "is_openrouter": is_openrouter # if true, use openrouter, else use openai
    }