from pathlib import Path
from src.agent.core import skye
from pydantic import Field
from pydantic_ai.tools import RunContext
from src.agent.deps import SkyeDeps
from typing import Annotated
import aiofiles

def resolve_safe(root: Path, user_path: str) -> Path:
    candidate = (root / user_path).resolve()
    if not candidate.is_relative_to(root.resolve()):
        raise ValueError(f"Path not in workspace: {user_path}")
    return candidate

@skye.tool
async def write_file_raw(
    ctx: RunContext[SkyeDeps],
    path: Annotated[Path, Field(description="The path where the file will be written")],
    content: Annotated[str, Field(description="The content of the file")]
) -> None:
    """Tool to write content to a file"""
    try:
        safe_path = resolve_safe(ctx.deps.workspace_root, path)
        async with aiofiles.open(safe_path, "w") as f:
            await f.write(content)
    except ValueError as e:
        print(e)

@skye.tool
async def read_file_raw(
    ctx: RunContext[SkyeDeps],
    path: Annotated[Path, Field(description="The path to the file you want to read")]
) -> str:
    """Tool to read a file"""
    try:
        safe_path = resolve_safe(ctx.deps.workspace_root, path)
        async with aiofiles.open(safe_path, "r") as f:
            return await f.read()
    except ValueError as e:
        print(e)