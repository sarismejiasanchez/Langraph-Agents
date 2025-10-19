from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

model = ChatGoogleGenerativeAI(model="gemini-2.5-pro")
agent = create_agent(model, [get_weather])