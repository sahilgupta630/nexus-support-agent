from pydantic import BaseModel

class EscalationBrief(BaseModel):
    customer_name: str
    issue_summary: str
    sentiment_history: list[str]
    suggested_tone: str

def analyze_sentiment(utterance: str) -> str:
    """
    Mock utterance-level sentiment detection.
    Returns: 'POSITIVE', 'NEUTRAL', or 'NEGATIVE'
    """
    negative_words = ["angry", "upset", "complain", "missing", "delay", "fraud", "bad", "worst"]
    if any(word in utterance.lower() for word in negative_words):
        return "NEGATIVE"
    return "NEUTRAL"

def check_escalation(sentiment_history: list[str]) -> bool:
    """
    Escalation Logic with carefully defined thresholds:
    Escalate if there are 2 consecutive negative sentiments in the history.
    """
    if len(sentiment_history) >= 2:
        if sentiment_history[-1] == "NEGATIVE" and sentiment_history[-2] == "NEGATIVE":
            return True
    return False

def generate_escalation_brief(customer_name: str, conversation_history: list[str], sentiment_history: list[str]) -> dict:
    """
    Instantly generates the escalation brief for the human agent.
    """
    summary = "Customer is repeatedly expressing negative sentiment regarding their issue."
    suggested_tone = "Empathetic, Apologetic, Assuring"
    
    return EscalationBrief(
        customer_name=customer_name,
        issue_summary=summary,
        sentiment_history=sentiment_history,
        suggested_tone=suggested_tone
    ).model_dump()
