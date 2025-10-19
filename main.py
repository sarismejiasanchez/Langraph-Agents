from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model=ChatGoogleGenerativeAI(model="gemini-2.5-pro"),
    tools=[get_weather],
    prompt="You are a helpful assistant",
)