from pydantic_ai.providers.openai import OpenAIProvider
from pydantic_ai.models.openai import OpenAIResponsesModel
from pydantic_ai import Agent
from dotenv import load_dotenv
import os, asyncio

load_dotenv()

skye = Agent(
    name="Skye",
    model=OpenAIResponsesModel(
        model_name="~deepseek/deepseek-v4-flash-latest",
        provider=OpenAIProvider(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY")
        )
    )
)

