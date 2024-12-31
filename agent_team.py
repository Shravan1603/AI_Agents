from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools

import os
from dotenv import load_dotenv

load_dotenv()

web_agent = Agent(
    name="We Agent",
    role="Search the web for information",
    model=OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,

)


finance_agent = Agent(
    name="Finance Agent",
    role="Get Financial data",
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True,company_info=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

agent_team = Agent(
    team=[web_agent, finance_agent],
    instructions=["Always Include Sources","Use Tables to display data"],
    show_tool_calls=True,
    markdown=True,
)


agent_team.print_response("Summarize analyst response ana share the latest news for NVDA",stream=True)
