from trafilatura import fetch_url, extract
from agent.core import skye
from pydantic import Field
from typing import Annotated

@skye.tool_plain
def fetch_page(
    url: Annotated[str, Field(description="The URL of the page you want to fetch")]
) -> str:
    """Tool to fetch content from a webpage"""
    
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