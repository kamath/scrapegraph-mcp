# ScrapeGraph MCP Server

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![smithery badge](https://smithery.ai/badge/@ScrapeGraphAI/scrapegraph-mcp)](https://smithery.ai/server/@ScrapeGraphAI/scrapegraph-mcp)

A [Model Context Protocol](https://modelcontextprotocol.io/introduction) (MCP) server that provides access to the [ScapeGraph AI](https://scrapegraphai.com) API. It allows language models to use AI-powered web scraping capabilities.

## Available Tools

The server exposes the following tools:

- `markdownify(website_url: str)`: Convert any webpage into clean, formatted markdown
- `smartscraper(user_prompt: str, website_url: str)`: Extract structured data from any webpage using AI
- `searchscraper(user_prompt: str)`: Perform AI-powered web searches with structured results

## Usage

You'll need a ScapeGraph API key to use this server. You can obtain one by:

1. Going to the [ScapeGraph Dashboard](https://dashboard.scrapegraphai.com)
2. Creating an account and obtaining an API key

### Installing via Smithery

To install ScrapeGraph API Integration Server for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@ScrapeGraphAI/scrapegraph-mcp):

```bash
npx -y @smithery/cli install @ScrapeGraphAI/scrapegraph-mcp --client claude
```

### Claude for Desktop

Update your `claude_desktop_config.json` (located in `~/Library/Application\ Support/Claude/claude_desktop_config.json` on macOS and `%APPDATA%/Claude/claude_desktop_config.json` on Windows) to include the following:

```json
{
    "mcpServers": {
        "scrapegraph": {
            "command": "uvx",
            "args": [
                "scrapegraph_mcp"
            ],
            "env": {
                "SGAI_API_KEY": "YOUR_SCRAPEGRAPH_API_KEY"
            }
        }
    }
}
```

## Example Queries

Once connected, you can ask Claude questions like:

- "What are the main features of the ScapeGraph API?"
- "Convert the ScapeGraph homepage into markdown"
- "Extract the pricing information from the ScapeGraph website"
- "Find information about the latest advancements in AI-powered web scraping"
- "Summarize the content of the Python documentation website"

## Error Handling

The server provides human-readable error messages for common issues:

- API authentication errors
- Invalid URL formats
- Network connectivity problems

## License

This project is licensed under the MIT License - see the LICENSE file for details. 