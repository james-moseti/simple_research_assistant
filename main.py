from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_deepseek import ChatDeepSeek
from langchain_anthropic import ChatAnthropic
from tools import search_tool, wiki_tool, save_tool
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor

load_dotenv()

# We'll define a class to specify which type of content we want our llm to generate
class ResearchResponse(BaseModel):
    """
    Specifying all the fields we want as output from the LLM call. 
    """
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

llm = ChatOpenAI(model="gpt-4o-mini")
llm2 = ChatDeepSeek(model="deepseek-chat", temperature=0,       # Can't be used here...
    max_tokens=None,
    timeout=None,
    max_retries=2,
    )

# response = model2.invoke("What is artificial intelligence?")
# print(response)

parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(      #TODO Check out more about this from the langchain docs
    [
        (
            "system",
            """
            You are a research assistant that will help generate a research paper. 
            Answer the user query and use the necessary tools. 
            Wrap the output in this format and provide no other text\n{format_instructions}
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())    # Partially going to fill in this prompt by passing the format instructions. 

tools = [search_tool, wiki_tool, save_tool]
agent = create_tool_calling_agent(
    llm = llm,
    prompt = prompt,
    tools = tools,
)

# Test our agent
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)  # Verbose refers to the thought process -> Use False if not needed. 
query = input("What can I help you research? ")
raw_response = agent_executor.invoke({"query": query})

try:
    structured_response = parser.parse(raw_response.get("output"))
    print(structured_response)
except Exception as e:
    print(f"Error parsing response {e} Raw Response - {raw_response}")