from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")


@mcp.tool()
def weather(location: str) -> str:
    """get weather for a location"""
    return "it's always raining in california"


mcp.run(transport="streamable-http")
