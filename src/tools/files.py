from pathlib import Path
from src.agent.core import skye
from pydantic import Field
from typing import Annotated
import aiofiles

def resolve_safe(root: Path, user_path: str) -> Path:
    candidate = (root / user_path).resolve()
    if not candidate.is_relative_to(root.resolve()):
        raise ValueError(f"Path not in workspace: {user_path}")
    return candidate

@skye.tool_plain
async def write_file_raw(
    path: Annotated[Path, Field(description="The path where the file will be written")],
    content: Annotated[str, Field(description="The content of the file")]
) -> None:
    """Tool to write content to a file"""
    async with aiofiles.open(path, "w") as f:
        await f.write(content)