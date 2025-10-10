# ScrapeGraph MCP Server

![ScapeGraph Smithery Integration](assets/sgai_smithery.png)
<a href="https://glama.ai/mcp/servers/37us0q2tr6">
  <img width="380" height="200" src="https://glama.ai/mcp/servers/37us0q2tr6/badge" alt="ScrapeGraph Server MCP server" style="display: inline-block;"/>
</a>
<a href="https://mseep.ai/app/scrapegraphai-scrapegraph-mcp">
  <img src="https://mseep.net/pr/scrapegraphai-scrapegraph-mcp-badge.png" alt="MseeP.ai Security Assessment Badge" style="display: inline-block;"/>
</a>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![smithery badge](https://smithery.ai/badge/@ScrapeGraphAI/scrapegraph-mcp)](https://smithery.ai/server/@ScrapeGraphAI/scrapegraph-mcp)


A production-ready [Model Context Protocol](https://modelcontextprotocol.io/introduction) (MCP) server that provides seamless integration with the [ScapeGraph AI](https://scrapegraphai.com) API. This server enables language models to leverage advanced AI-powered web scraping capabilities with enterprise-grade reliability.


## Available Tools

The server provides the following enterprise-ready tools:

### Core Scraping Tools

- `markdownify(website_url: str)`: Transform any webpage into clean, structured markdown format
- `smartscraper(user_prompt: str, website_url: str, number_of_scrolls: int = None, markdown_only: bool = None)`: Leverage AI to extract structured data from any webpage with support for infinite scrolling
- `searchscraper(user_prompt: str, num_results: int = None, number_of_scrolls: int = None)`: Execute AI-powered web searches with structured, actionable results

### Advanced Scraping Tools

- `scrape(website_url: str, render_heavy_js: bool = None)`: Basic scraping endpoint to fetch page content with optional heavy JavaScript rendering
- `sitemap(website_url: str)`: Extract sitemap URLs and structure for any website

### Multi-Page Crawling

- `smartcrawler_initiate(url: str, prompt: str = None, extraction_mode: str = "ai", depth: int = None, max_pages: int = None, same_domain_only: bool = None)`: Initiate intelligent multi-page web crawling with two modes:
  - **AI Extraction Mode** (10 credits per page): Extracts structured data based on your prompt
  - **Markdown Conversion Mode** (2 credits per page): Converts pages to clean markdown
- `smartcrawler_fetch_results(request_id: str)`: Retrieve results from asynchronous crawling operations

### Intelligent Agent-Based Scraping

- `agentic_scrapper(url: str, user_prompt: str = None, output_schema: dict = None, steps: list = None, ai_extraction: bool = None, persistent_session: bool = None, timeout_seconds: float = None)`: Run advanced agentic scraping workflows with customizable steps and structured output schemas

## Setup Instructions

To utilize this server, you'll need a ScapeGraph API key. Follow these steps to obtain one:

1. Navigate to the [ScapeGraph Dashboard](https://dashboard.scrapegraphai.com)
2. Create an account and generate your API key

### Automated Installation via Smithery

For automated installation of the ScrapeGraph API Integration Server using [Smithery](https://smithery.ai/server/@ScrapeGraphAI/scrapegraph-mcp):

```bash
npx -y @smithery/cli install @ScrapeGraphAI/scrapegraph-mcp --client claude
```

### Claude Desktop Configuration

Update your Claude Desktop configuration file with the following settings (located on the top rigth of the Cursor page):

(remember to add your API key inside the config)

```json
{
    "mcpServers": {
        "@ScrapeGraphAI-scrapegraph-mcp": {
            "command": "npx",
            "args": [
                "-y",
                "@smithery/cli@latest",
                "run",
                "@ScrapeGraphAI/scrapegraph-mcp",
                "--config",
                "\"{\\\"scrapegraphApiKey\\\":\\\"YOUR-SGAI-API-KEY\\\"}\""
            ]
        }
    }
}
```

The configuration file is located at:
- Windows: `%APPDATA%/Claude/claude_desktop_config.json`
- macOS: `~/Library/Application\ Support/Claude/claude_desktop_config.json`

### Cursor Integration

Add the ScrapeGraphAI MCP server on the settings:

![Cursor MCP Integration](assets/cursor_mcp.png)

## Example Use Cases

The server enables sophisticated queries such as:

### Single Page Scraping
- "Analyze and extract the main features of the ScapeGraph API"
- "Generate a structured markdown version of the ScapeGraph homepage"
- "Extract and analyze pricing information from the ScapeGraph website with infinite scroll support"
- "Scrape this JavaScript-heavy page with full rendering"

### Search and Research
- "Research and summarize recent developments in AI-powered web scraping"
- "Search for the top 5 articles about machine learning frameworks and extract key points"

### Multi-Page Crawling
- "Crawl the entire documentation site and convert all pages to markdown"
- "Extract all product information from an e-commerce site up to 3 levels deep"
- "Crawl a blog and extract all article titles, authors, and summaries"

### Advanced Agentic Scraping
- "Navigate through a multi-step form and extract the final results"
- "Follow pagination links and compile a complete dataset"
- "Execute a complex workflow with custom extraction schema"

## Error Handling

The server implements robust error handling with detailed, actionable error messages for:

- API authentication issues
- Malformed URL structures
- Network connectivity failures
- Rate limiting and quota management

## Common Issues

### Windows-Specific Connection

When running on Windows systems, you may need to use the following command to connect to the MCP server:

```bash
C:\Windows\System32\cmd.exe /c npx -y @smithery/cli@latest run @ScrapeGraphAI/scrapegraph-mcp --config "{\"scrapegraphApiKey\":\"YOUR-SGAI-API-KEY\"}"
```

This ensures proper execution in the Windows environment.

## License

This project is distributed under the MIT License. For detailed terms and conditions, please refer to the LICENSE file.

## Acknowledgments

Special thanks to [tomekkorbak](https://github.com/tomekkorbak) for his implementation of [oura-mcp-server](https://github.com/tomekkorbak/oura-mcp-server), which served as starting point for this repo.

Made with ❤️ by [ScrapeGraphAI](https://scrapegraphai.com) Team
