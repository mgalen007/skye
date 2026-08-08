from pydantic_ai.providers.openai import OpenAIProvider
from pydantic_ai.models.openai import OpenAIResponsesModel
from pydantic_ai import Agent
from pydantic_ai.capabilities import WebSearch
from dotenv import load_dotenv
from src.agent.deps import SkyeDeps
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
    ),
    capabilities=[WebSearch()],
    deps_type=SkyeDeps
)

if __name__ == "__main__":
    async def test_agent():
        result = await skye.run("Write me a haiku about H.E Paul Kagame")
        print(result.output)
    asyncio.run(test_agent())