#!/usr/bin/env python3
"""
MCP server for ScapeGraph API integration.
This server exposes methods to use ScapeGraph's AI-powered web scraping services:
- markdownify: Convert any webpage into clean, formatted markdown
- smartscraper: Extract structured data from any webpage using AI
- searchscraper: Perform AI-powered web searches with structured results
"""

import os
from typing import Any, Dict

import httpx
from mcp.server.fastmcp import FastMCP


class ScapeGraphClient:
    """Client for interacting with the ScapeGraph API."""

    BASE_URL = "https://api.scrapegraphai.com/v1"

    def __init__(self, api_key: str):
        """
        Initialize the ScapeGraph API client.

        Args:
            api_key: API key for ScapeGraph API
        """
        self.api_key = api_key
        self.headers = {
            "SGAI-APIKEY": api_key,
            "Content-Type": "application/json"
        }
        self.client = httpx.Client(timeout=60.0)

    def markdownify(self, website_url: str) -> Dict[str, Any]:
        """
        Convert a webpage into clean, formatted markdown.

        Args:
            website_url: URL of the webpage to convert

        Returns:
            Dictionary containing the markdown result
        """
        url = f"{self.BASE_URL}/markdownify"
        data = {
            "website_url": website_url
        }

        response = self.client.post(url, headers=self.headers, json=data)

        if response.status_code != 200:
            error_msg = f"Error {response.status_code}: {response.text}"
            raise Exception(error_msg)

        return response.json()

    def smartscraper(self, user_prompt: str, website_url: str) -> Dict[str, Any]:
        """
        Extract structured data from a webpage using AI.

        Args:
            user_prompt: Instructions for what data to extract
            website_url: URL of the webpage to scrape

        Returns:
            Dictionary containing the extracted data
        """
        url = f"{self.BASE_URL}/smartscraper"
        data = {
            "user_prompt": user_prompt,
            "website_url": website_url
        }

        response = self.client.post(url, headers=self.headers, json=data)

        if response.status_code != 200:
            error_msg = f"Error {response.status_code}: {response.text}"
            raise Exception(error_msg)

        return response.json()

    def searchscraper(self, user_prompt: str) -> Dict[str, Any]:
        """
        Perform AI-powered web searches with structured results.

        Args:
            user_prompt: Search query or instructions

        Returns:
            Dictionary containing search results and reference URLs
        """
        url = f"{self.BASE_URL}/searchscraper"
        data = {
            "user_prompt": user_prompt
        }

        response = self.client.post(url, headers=self.headers, json=data)

        if response.status_code != 200:
            error_msg = f"Error {response.status_code}: {response.text}"
            raise Exception(error_msg)

        return response.json()

    def close(self) -> None:
        """Close the HTTP client."""
        self.client.close()


# Create MCP server
mcp = FastMCP("ScapeGraph API MCP Server")

# Default API key (will be overridden in main or by direct assignment)
default_api_key = os.environ.get("SGAI_API_KEY")
scrapegraph_client = ScapeGraphClient(default_api_key) if default_api_key else None


# Add tool for markdownify
@mcp.tool()
def markdownify(website_url: str) -> Dict[str, Any]:
    """
    Convert a webpage into clean, formatted markdown.

    Args:
        website_url: URL of the webpage to convert

    Returns:
        Dictionary containing the markdown result
    """
    if scrapegraph_client is None:
        return {"error": "ScapeGraph client not initialized. Please provide an API key."}

    try:
        return scrapegraph_client.markdownify(website_url)
    except Exception as e:
        return {"error": str(e)}


# Add tool for smartscraper
@mcp.tool()
def smartscraper(
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
    if scrapegraph_client is None:
        return {"error": "ScapeGraph client not initialized. Please provide an API key."}

    try:
        return scrapegraph_client.smartscraper(user_prompt, website_url)
    except Exception as e:
        return {"error": str(e)}


# Add tool for searchscraper
@mcp.tool()
def searchscraper(
    user_prompt: str
) -> Dict[str, Any]:
    """
    Perform AI-powered web searches with structured results.

    Args:
        user_prompt: Search query or instructions

    Returns:
        Dictionary containing search results and reference URLs
    """
    if scrapegraph_client is None:
        return {"error": "ScapeGraph client not initialized. Please provide an API key."}

    try:
        return scrapegraph_client.searchscraper(user_prompt)
    except Exception as e:
        return {"error": str(e)}


def main() -> None:
    """Run the ScapeGraph MCP server."""
    print("Starting ScapeGraph MCP server!")
    # Run the server
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main() 