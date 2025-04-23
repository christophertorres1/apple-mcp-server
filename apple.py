from mcp.server.fastmcp import FastMCP

mcp = FastMCP("apple")


@mcp.tool()
def hello():
    """Say hello."""
    return "Hello from Apple MCP!"


if __name__ == "__main__":
    mcp.run()
