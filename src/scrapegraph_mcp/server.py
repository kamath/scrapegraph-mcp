#!/usr/bin/env python3
"""
MCP server for ScapeGraph API integration.
This server exposes methods to use ScapeGraph's AI-powered web scraping services:
- markdownify: Convert any webpage into clean, formatted markdown
- smartscraper: Extract structured data from any webpage using AI
- searchscraper: Perform AI-powered web searches with structured results
"""

import os
import sys
import logging
import traceback
from typing import Any, Dict

import httpx
from mcp.server.fastmcp import FastMCP


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stderr)
    ]
)
logger = logging.getLogger("scrapegraph_mcp")


class ScapeGraphClient:
    """Client for interacting with the ScapeGraph API."""

    BASE_URL = "https://api.scrapegraphai.com/v1"

    def __init__(self, api_key: str):
        """
        Initialize the ScapeGraph API client.

        Args:
            api_key: API key for ScapeGraph API
        """
        logger.info("Initializing ScapeGraphClient")
        self.api_key = api_key
        self.headers = {
            "SGAI-APIKEY": api_key,
            "Content-Type": "application/json"
        }
        self.client = httpx.Client(timeout=60.0)
        logger.info("ScapeGraphClient initialized successfully")

    def markdownify(self, website_url: str) -> Dict[str, Any]:
        """
        Convert a webpage into clean, formatted markdown.

        Args:
            website_url: URL of the webpage to convert

        Returns:
            Dictionary containing the markdown result
        """
        logger.info(f"Calling markdownify for URL: {website_url}")
        url = f"{self.BASE_URL}/markdownify"
        data = {
            "website_url": website_url
        }

        try:
            logger.debug(f"Making POST request to {url}")
            response = self.client.post(url, headers=self.headers, json=data)
            
            if response.status_code != 200:
                error_msg = f"Error {response.status_code}: {response.text}"
                logger.error(f"API request failed: {error_msg}")
                raise Exception(error_msg)
            
            logger.info("markdownify request successful")
            return response.json()
        except Exception as e:
            logger.error(f"Exception in markdownify: {str(e)}")
            raise

    def smartscraper(self, user_prompt: str, website_url: str) -> Dict[str, Any]:
        """
        Extract structured data from a webpage using AI.

        Args:
            user_prompt: Instructions for what data to extract
            website_url: URL of the webpage to scrape

        Returns:
            Dictionary containing the extracted data
        """
        logger.info(f"Calling smartscraper for URL: {website_url} with prompt: {user_prompt}")
        url = f"{self.BASE_URL}/smartscraper"
        data = {
            "user_prompt": user_prompt,
            "website_url": website_url
        }

        try:
            logger.debug(f"Making POST request to {url}")
            response = self.client.post(url, headers=self.headers, json=data)
            
            if response.status_code != 200:
                error_msg = f"Error {response.status_code}: {response.text}"
                logger.error(f"API request failed: {error_msg}")
                raise Exception(error_msg)
            
            logger.info("smartscraper request successful")
            return response.json()
        except Exception as e:
            logger.error(f"Exception in smartscraper: {str(e)}")
            raise

    def searchscraper(self, user_prompt: str) -> Dict[str, Any]:
        """
        Perform AI-powered web searches with structured results.

        Args:
            user_prompt: Search query or instructions

        Returns:
            Dictionary containing search results and reference URLs
        """
        logger.info(f"Calling searchscraper with prompt: {user_prompt}")
        url = f"{self.BASE_URL}/searchscraper"
        data = {
            "user_prompt": user_prompt
        }

        try:
            logger.debug(f"Making POST request to {url}")
            response = self.client.post(url, headers=self.headers, json=data)
            
            if response.status_code != 200:
                error_msg = f"Error {response.status_code}: {response.text}"
                logger.error(f"API request failed: {error_msg}")
                raise Exception(error_msg)
            
            logger.info("searchscraper request successful")
            return response.json()
        except Exception as e:
            logger.error(f"Exception in searchscraper: {str(e)}")
            raise

    def close(self) -> None:
        """Close the HTTP client."""
        logger.info("Closing ScapeGraphClient")
        self.client.close()
        logger.info("ScapeGraphClient closed")


# Log environment information
logger.info(f"Python version: {sys.version}")
logger.info(f"Current working directory: {os.getcwd()}")
logger.info(f"PATH environment variable: {os.environ.get('PATH', 'Not set')}")

# Create MCP server
logger.info("Creating MCP server")
mcp = FastMCP("ScapeGraph API MCP Server")
logger.info("MCP server created")

# Default API key (will be overridden in main or by direct assignment)
default_api_key = os.environ.get("SGAI_API_KEY")
logger.info(f"SGAI_API_KEY environment variable is {'set' if default_api_key else 'not set'}")

scrapegraph_client = None
if default_api_key:
    try:
        logger.info("Initializing ScapeGraphClient with default API key")
        scrapegraph_client = ScapeGraphClient(default_api_key)
        logger.info("ScapeGraphClient initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize ScapeGraphClient: {str(e)}")
        logger.error(traceback.format_exc())


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
    logger.info(f"Tool markdownify called with URL: {website_url}")
    
    if scrapegraph_client is None:
        logger.warning("ScapeGraph client not initialized")
        return {"error": "ScapeGraph client not initialized. Please provide an API key."}

    try:
        result = scrapegraph_client.markdownify(website_url)
        logger.info("markdownify tool call successful")
        return result
    except Exception as e:
        logger.error(f"Error in markdownify tool: {str(e)}")
        logger.error(traceback.format_exc())
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
    logger.info(f"Tool smartscraper called with URL: {website_url} and prompt: {user_prompt}")
    
    if scrapegraph_client is None:
        logger.warning("ScapeGraph client not initialized")
        return {"error": "ScapeGraph client not initialized. Please provide an API key."}

    try:
        result = scrapegraph_client.smartscraper(user_prompt, website_url)
        logger.info("smartscraper tool call successful")
        return result
    except Exception as e:
        logger.error(f"Error in smartscraper tool: {str(e)}")
        logger.error(traceback.format_exc())
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
    logger.info(f"Tool searchscraper called with prompt: {user_prompt}")
    
    if scrapegraph_client is None:
        logger.warning("ScapeGraph client not initialized")
        return {"error": "ScapeGraph client not initialized. Please provide an API key."}

    try:
        result = scrapegraph_client.searchscraper(user_prompt)
        logger.info("searchscraper tool call successful")
        return result
    except Exception as e:
        logger.error(f"Error in searchscraper tool: {str(e)}")
        logger.error(traceback.format_exc())
        return {"error": str(e)}


def main() -> None:
    """Run the ScapeGraph MCP server."""
    try:
        logger.info("Starting ScapeGraph MCP server!")
        print("Starting ScapeGraph MCP server!", file=sys.stderr)
        
        # Log system information
        logger.info(f"Python executable: {sys.executable}")
        logger.info(f"Arguments: {sys.argv}")
        
        # Run the server
        logger.info("Running MCP server with stdio transport")
        mcp.run(transport="stdio")
    except Exception as e:
        logger.critical(f"Fatal error in main: {str(e)}")
        logger.critical(traceback.format_exc())
        print(f"Fatal error: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main() 