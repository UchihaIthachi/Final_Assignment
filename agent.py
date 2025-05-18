from config import settings
from llm_provider import get_llm
from tools import ALL_TOOLS
from retrievers import custom_retriever
from langgraph.graph import START, StateGraph, MessagesState
from langgraph.prebuilt import tools_condition, ToolNode
from langchain_core.messages import SystemMessage, HumanMessage

# Load system prompt
with open(settings.system_prompt_path, "r", encoding="utf-8") as f:
    system_prompt = f.read()

sys_msg = SystemMessage(content=system_prompt)

def build_graph():
    llm = get_llm(settings.llm_provider)
    llm_with_tools = llm.bind_tools(ALL_TOOLS)
    
    def assistant(state: MessagesState):
        return {"messages": [llm_with_tools.invoke(state["messages"])]}

    def retriever(state: MessagesState):
        similar_q = custom_retriever.retrieve(state["messages"][0].content)
        example_msg = HumanMessage(content=f"Similar Q&A:\n\n{similar_q}")
        return {"messages": [sys_msg] + state["messages"] + [example_msg]}

    builder = StateGraph(MessagesState)
    builder.add_node("retriever", retriever)
    builder.add_node("assistant", assistant)
    builder.add_node("tools", ToolNode(ALL_TOOLS))
    builder.add_edge(START, "retriever")
    builder.add_edge("retriever", "assistant")
    builder.add_conditional_edges("assistant", tools_condition)
    builder.add_edge("tools", "assistant")

    return builder.compile()

if __name__ == "__main__":
    graph = build_graph()
    question = input("Ask your question: ")
    messages = [HumanMessage(content=question)]
    results = graph.invoke({"messages": messages})
    for m in results["messages"]:
        print(m.content)