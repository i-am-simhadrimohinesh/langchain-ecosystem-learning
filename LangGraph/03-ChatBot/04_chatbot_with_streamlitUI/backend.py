from langgraph.graph import StateGraph,START,END
from langgraph.checkpoint.memory import InMemorySaver
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage,AIMessage
from dotenv import load_dotenv
from typing import TypedDict
import os

os.environ["LANGCHAIN_VERBOSE"] = "true"

class ChatState(TypedDict):
    result : str
    prompt : str
    history : list

load_dotenv()

chatmodel = ChatGoogleGenerativeAI(model='gemini-3.5-flash')
# chatmodel = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

def llmcall(state):
    history = state.get("history", [])   
    history.append(HumanMessage(state['prompt']))
    res = chatmodel.invoke(history)
    state['result'] = res.content[0]['text']
    
    history.append(AIMessage(state['result']))
    state['history'] = history
    return state

graph = StateGraph(ChatState)
graph.add_node('llmcall',llmcall)
graph.add_edge(START,'llmcall')
graph.add_edge('llmcall',END)
checkpointer = InMemorySaver()
chatbot = graph.compile(checkpointer=checkpointer)
res = chatbot.invoke({'prompt':"Hi","history":[]},config={
    "configurable": {
        "thread_id": "user-123"
    }})['result']
print(res)