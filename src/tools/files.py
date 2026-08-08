from pathlib import Path

def resolve_safe(root: Path, user_path: str) -> Path:
    candidate = (root / user_path).resolve()
    if not candidate.is_relative_to(root.resolve()):
        raise ValueError(f"Path not in workspace: {user_path}")
    return candidate