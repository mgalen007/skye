from pathlib import Path
from src.agent.core import skye
from pydantic import Field
from pydantic_ai.tools import RunContext
from pydantic_ai import ModelRetry
from src.agent.deps import SkyeDeps
from typing import Annotated
import aiofiles

def resolve_safe(root: Path, user_path: Path) -> Path:
    if user_path.is_absolute():
        raise ValueError(f"Absolute paths not allowed: {user_path}")
    candidate = (root / user_path).resolve()
    if not candidate.is_relative_to(root):
        raise ValueError(f"Path not in workspace: {user_path}")
    return candidate

@skye.tool
async def write_file_raw(
    ctx: RunContext[SkyeDeps],
    path: Annotated[Path, Field(description="The path where the file will be written")],
    content: Annotated[str, Field(description="The content of the file")]
) -> str:
    """Tool to write content to a file"""
    try:
        safe_path = resolve_safe(ctx.deps.workspace_root, path)
    except ValueError as e:
        raise ModelRetry(str(e)) from e

    try:
        safe_path.parent.mkdir(parents=True, exist_ok=True)
        async with aiofiles.open(safe_path, "w") as f:
            await f.write(content)
        return f"Wrote {len(content)} characters to {safe_path}"
    except OSError as e:
        raise ModelRetry(f"Failed to write {path}: {e}") from e

@skye.tool
async def read_file_raw(
    ctx: RunContext[SkyeDeps],
    path: Annotated[Path, Field(description="The path to the file you want to read")]
) -> str:
    """Tool to read a file"""
    try:
        safe_path = resolve_safe(ctx.deps.workspace_root, path)
    except ValueError as e:
        raise ModelRetry(str(e)) from e

    try: 
        async with aiofiles.open(safe_path, "r") as f:
            return await f.read()
    except OSError as e:
        raise ModelRetry(f"Failed to read {safe_path}: {e}") from e