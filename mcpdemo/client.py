from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import asyncio

load_dotenv()


async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": [
                    "/Users/poojaveluri/Documents/agentic-ai/mcpdemo/mathserver.py"
                ],
                "transport": "stdio",
            },
            "weather": {
                "url": "http://127.0.0.1:8000/mcp",
                "transport": "streamable_http",
            },
        }
    )

    tools = await client.get_tools()

    llm = ChatGroq(model="openai/gpt-oss-120b")

    agent = create_react_agent(model=llm, tools=tools)

    response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "What is (3+5)*2"}]}
    )

    print(response["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
