from agent.core import skye
from agent.deps import SkyeDeps
from rich import print
from rich.prompt import Prompt
import tools.files
import tools.fetch
import asyncio

async def loop():
    message_history = []

    while True:
        prompt = Prompt.ask("[bold cyan]User[/bold cyan]")
        result = await skye.run(
            prompt, 
            deps=SkyeDeps(workspace_root="./workspace"), 
            message_history=message_history
        )
        message_history = result.all_messages()
        print(f"[bold red]Skye: [/bold red]{result.output}")

if __name__ == "__main__":
    asyncio.run(loop())