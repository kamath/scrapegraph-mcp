#!/usr/bin/env python3
"""
MCP server for ScapeGraph API integration.
This server exposes methods to use ScapeGraph's AI-powered web scraping services:
- markdownify: Convert any webpage into clean, formatted markdown
- smartscraper: Extract structured data from any webpage using AI
- searchscraper: Perform AI-powered web searches with structured results
"""

import os
import asyncio
from typing import Any, Dict, Optional

from mcp.server.fastmcp import FastMCP
from scrapegraph_py import AsyncClient


class ScapeGraphAsyncClient:
    """Async wrapper for the ScapeGraph Python SDK."""

    def __init__(self, api_key: str):
        """
        Initialize the ScapeGraph async client.

        Args:
            api_key: API key for ScapeGraph API
        """
        self.client = AsyncClient(api_key=api_key)

    async def markdownify(self, website_url: str) -> Dict[str, Any]:
        """
        Convert a webpage into clean, formatted markdown.

        Args:
            website_url: URL of the webpage to convert

        Returns:
            Dictionary containing the markdown result
        """
        return await self.client.markdownify(website_url=website_url)

    async def smartscraper(
        self, 
        user_prompt: str, 
        website_url: str
    ) -> Dict[str, Any]:
        """
        Extract structured data from a webpage using AI.

        Args:
            user_prompt: Instructions for what data to extract
            website_url: URL of the webpage to scrape

        Returns:
            Dictionary containing the extracted data
        """
        return await self.client.smartscraper(
            user_prompt=user_prompt,
            website_url=website_url
        )

    async def searchscraper(
        self,
        user_prompt: str
    ) -> Dict[str, Any]:
        """
        Perform AI-powered web searches with structured results.

        Args:
            user_prompt: Search query or instructions

        Returns:
            Dictionary containing search results and reference URLs
        """
        return await self.client.searchscraper(
            user_prompt=user_prompt
        )

    async def close(self) -> None:
        """Close the client to free up resources."""
        await self.client.close()


# Create MCP server and AsyncScapeGraphWrapper at module level
mcp = FastMCP("ScapeGraph API MCP Server")

# Default API key (will be overridden in main or by direct assignment)
default_api_key = os.environ.get("SGAI_API_KEY")
scrapegraph_wrapper = ScapeGraphAsyncClient(default_api_key) if default_api_key else None


# Add tools for markdownify
@mcp.tool()
async def markdownify(website_url: str) -> Dict[str, Any]:
    """
    Convert a webpage into clean, formatted markdown.

    Args:
        website_url: URL of the webpage to convert

    Returns:
        Dictionary containing the markdown result
    """
    if scrapegraph_wrapper is None:
        return {"error": "ScapeGraph client not initialized. Please provide an API key."}

    try:
        return await scrapegraph_wrapper.markdownify(website_url)
    except Exception as e:
        return {"error": str(e)}


# Add tools for smartscraper
@mcp.tool()
async def smartscraper(
    user_prompt: str, 
    website_url: str
) -> Dict[str, Any]:
    """
    Extract structured data from a webpage using AI.

    Args:
        user_prompt: Instructions for what data to extract
        website_url: URL of the webpage to scrape

    Returns:
        Dictionary containing the extracted data
    """
    if scrapegraph_wrapper is None:
        return {"error": "ScapeGraph client not initialized. Please provide an API key."}

    try:
        return await scrapegraph_wrapper.smartscraper(user_prompt, website_url)
    except Exception as e:
        return {"error": str(e)}


# Add tools for searchscraper
@mcp.tool()
async def searchscraper(
    user_prompt: str
) -> Dict[str, Any]:
    """
    Perform AI-powered web searches with structured results.

    Args:
        user_prompt: Search query or instructions

    Returns:
        Dictionary containing search results and reference URLs
    """
    if scrapegraph_wrapper is None:
        return {"error": "ScapeGraph client not initialized. Please provide an API key."}

    try:
        return await scrapegraph_wrapper.searchscraper(user_prompt)
    except Exception as e:
        return {"error": str(e)}


async def cleanup() -> None:
    """Clean up resources when the server is shutting down."""
    if scrapegraph_wrapper is not None:
        await scrapegraph_wrapper.close()


def main() -> None:
    """Run the ScapeGraph MCP server."""
    print("Starting ScapeGraph MCP server!")
    # Run the server
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main() 