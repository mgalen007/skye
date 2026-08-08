from agent.core import skye
from rich import print
from rich.prompt import Prompt
import asyncio

async def loop():
    while True:
        prompt = Prompt.ask("[bold cyan]User[/bold cyan]")
        result = await skye.run(prompt)
        print(f"[bold red]Skye: [/bold red]{result.output}")

if __name__ == "__main__":
    asyncio.run(loop())