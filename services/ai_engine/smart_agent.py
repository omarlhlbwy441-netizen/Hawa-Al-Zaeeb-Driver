from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
import os

# تهيئة قاعدة البيانات المتجهية
embeddings = OpenAIEmbeddings()
db = Chroma(persist_directory="services/ai_engine/vector_store", embedding_function=embeddings)

def search_knowledge_base(query: str) -> str:
    '''أداة للبحث في وثائق النظام والمعرفة الخاصة'''
    docs = db.similarity_search(query, k=2)
    return "\n".join([doc.page_content for doc in docs])

def build_advanced_agent():
    llm = ChatOpenAI(temperature=0, model="gpt-4")
    
    tools = [
        Tool(
            name="KnowledgeBaseSearch",
            func=search_knowledge_base,
            description="استخدم هذه الأداة للبحث عن معلومات حول سياسات الشركة، المنتجات، أو الدعم الفني."
        )
    ]
    
    return initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )

agent_executor = build_advanced_agent()