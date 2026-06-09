from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import init_chat_model
from langchain.prompts import PromptTemplate
from services.rag import query_rag
from database.mock_db import get_order_details, initiate_return

# Memory dictionary to map session_id -> Memory and Sentiment list
session_store = {}

def get_session(session_id: str):
    if session_id not in session_store:
        session_store[session_id] = {
            "memory": ConversationBufferMemory(return_messages=True),
            "sentiment_history": [],
            "customer_name": "Valued Customer" # Mapped from context in prod
        }
    return session_store[session_id]

def process_intent_routing(text: str) -> str:
    """
    Hybrid routing approach. In production, this uses an LLM Router.
    Intents: order_status, return_refund, payment_issue, delivery_complaint, product_query
    """
    text_lower = text.lower()
    if "order" in text_lower and "ord" in text_lower:
        # Extract ID
        words = text_lower.split()
        for w in words:
            if w.startswith("ord"):
                details = get_order_details(w)
                if details:
                    return f"System Info: The user's order {w} is currently {details['status']} and expected on {details['delivery_date']}."
        return "System Info: Ask the user for their valid order ID."
    
    elif "return" in text_lower or "policy" in text_lower or "refund" in text_lower:
        rag_context = query_rag("return policy")
        return f"System Info: Corporate Policy state: {rag_context}"
    
    return "System Info: No specific database context needed."

def handle_user_message(session_id: str, message: str) -> dict:
    """
    Main conversaton engine handling multi-turn capabilities and retaining context.
    """
    session = get_session(session_id)
    
    # Analyze Sentiment before processing
    from services.sentiment import analyze_sentiment, check_escalation, generate_escalation_brief
    sent = analyze_sentiment(message)
    session["sentiment_history"].append(sent)
    
    escalated = False
    brief = None
    
    if check_escalation(session["sentiment_history"]):
        escalated = True
        brief = generate_escalation_brief(
            session["customer_name"],
            [], # Mapped from memory in active prod
            session["sentiment_history"]
        )
        return {
            "response": "I apologize that you are experiencing this. I am escalating your query to a human agent who will connect with you right away.",
            "escalated": True,
            "escalation_brief": brief
        }
    
    # Context injected via intent routing RAG
    injected_context = process_intent_routing(message)
    
    # Create the internal prompt for the LLM
    internal_prompt = f"Context: {injected_context}\nUser says: {message}\nProvide a helpful, empathetic response."
    
    # Note: In production we use Gemini via ChatGoogleGenerativeAI
    # Here we simulate the LLM Agent response due to missing API keys.
    bot_reply = "I understand you need help with your issue. Could you provide a bit more detail?"
    
    # Hardcoded responses for demonstration based on intent context
    if "Shipped" in injected_context:
        bot_reply = "I checked your order! It is currently shipped and will arrive as scheduled."
    elif "policy" in injected_context:
        bot_reply = "Our policy allows returns within 30 days. Would you like me to initiate one?"
    
    # Store in memory
    session["memory"].chat_memory.add_user_message(message)
    session["memory"].chat_memory.add_ai_message(bot_reply)
    
    return {
        "response": bot_reply,
        "escalated": False,
        "escalation_brief": None
    }
