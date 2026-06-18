from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType
import os

os.environ["OPENAI_API_KEY"] = "your-openai-api-key-here"

def check_order_status(order_id_str: str) -> str:
    try:
        order_id = int(order_id_str)
        return f"الطلب رقم {order_id} قيد التجهيز (Processing) وسيتم شحنه قريباً."
    except Exception:
        return "عذراً، لم أتمكن من العثور على هذا الطلب، يرجى التأكد من الرقم."

def build_customer_service_agent():
    llm = ChatOpenAI(temperature=0.3, model="gpt-4")
    tools = [
        Tool(
            name="CheckOrderStatus",
            func=check_order_status,
            description="استخدم هذه الأداة عندما يسأل العميل عن حالة طلبه. يجب تمرير رقم الطلب."
        )
    ]
    return initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

agent_executor = build_customer_service_agent()