from dataclasses import dataclass
from pathlib import Path

@dataclass
class SkyeDeps:
    workspace_root: Path
    
    def __post_init__(self):
        self.workspace_root = Path(self.workspace_root).expanduser().resolve()