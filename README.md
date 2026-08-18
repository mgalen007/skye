# Skye

Skye is a small CLI assistant built with PydanticAI. The rebuild is moving Skye from a narrow demo agent into a general-purpose command-line assistant that can answer natural-language requests, search the web through the model provider, and work with files inside a local sandboxed workspace.

## Current Status

Implemented:

- PydanticAI agent named `Skye`
- OpenRouter-backed model configuration through `OPENROUTER_API_KEY`
- Rich-powered interactive CLI loop
- In-session conversation history via `result.all_messages()`
- Sandboxed file tools:
  - `write_file`
  - `read_file`
  - `get_cwd`
- `fetch_page` web fetch/extraction tool using `trafilatura`
- Workspace path protection that rejects absolute paths and path traversal outside `./workspace`
- PydanticAI `WebSearch` capability enabled on the agent

Scaffolded or planned:

- `make_dir` and `list_dir` tools
- Cross-session memory with Chroma
- Rich streaming/status polish for tool calls
- History trimming for long sessions
- Open-source release polish, including `.env.example`, tests, license, and contribution docs

## Project Layout

```text
src/
  main.py              # Interactive CLI entry point
  agent/
    core.py            # Skye agent definition and model/provider setup
    deps.py            # Runtime dependencies passed into tools
  tools/
    files.py           # Sandboxed workspace file tools
    fetch.py           # Planned fetch/extraction tools
    memory_tools.py    # Planned memory tools
  memory/              # Planned Chroma-backed memory layer
  session/             # Planned session/history helpers
  ui/                  # Planned Rich UI helpers

workspace/             # Files Skye is allowed to read/write at runtime
chroma_data/           # Planned local Chroma persistence
PLAN.md                # Rebuild roadmap
```

## Requirements

- Python `>=3.14`
- `uv`
- An OpenRouter API key

Dependencies are managed in `pyproject.toml` and locked in `uv.lock`.

## Setup

Install dependencies:

```powershell
uv sync
```

Create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=your_openrouter_key_here
```

The current model is configured in `src/agent/core.py`:

```python
model_name="~deepseek/deepseek-v4-flash-latest"
```

## Running Skye

Start the CLI:

```powershell
uv run python src/main.py
```

You will get a prompt like:

```text
User:
```

Try requests such as:

```text
Write a short note in notes/hello.txt
Read notes/hello.txt back to me
Search the web for recent Python packaging news and summarize it
```

## Workspace Safety

Skye's file tools resolve all paths against `./workspace`.

Allowed examples:

```text
notes/hello.txt
research/top-10-richest/person-01.md
```

Rejected examples:

```text
C:\Users\HP\secret.txt
/etc/passwd
../../outside-workspace.txt
```

This keeps agent-written files contained to the project workspace.

## Development Roadmap

The next practical steps are:

1. Add `make_dir` and `list_dir` to complete the basic file-tool set.
2. Implement `fetch_page` in `src/tools/fetch.py` using `trafilatura`.
3. Register fetch and memory tools from the CLI entry point.
4. Add a populated `.env.example`.
5. Add focused tests for workspace path safety.
6. Add Chroma-backed `remember_fact` and top-k recall injection once core search/fetch workflows are stable.

## Notes

This repo is still in an early rebuild phase. The README reflects the current code rather than the full intended product, so planned modules may exist as empty scaffolds until their checkpoint is implemented.
