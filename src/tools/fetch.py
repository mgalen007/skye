from trafilatura import fetch_url, extract
from agent.core import skye
from pydantic import Field
from typing import Annotated
from pydantic_ai import ModelRetry

@skye.tool_plain
def fetch_page(
    url: Annotated[str, Field(description="The URL of the page you want to fetch")]
) -> str:
    """Tool to fetch content from a webpage"""
    try:    
        print("Using tool: fetch_page")
        downloaded = fetch_url(url)

        result = extract(
            filecontent=downloaded,
            include_links=True,
            include_comments=False,
            include_images=False,
            output_format="markdown"
        )

        return result 
    except Exception as e:
        raise ModelRetry(f"Failed to fetch: {e}") from e