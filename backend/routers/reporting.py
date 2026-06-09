from fastapi import APIRouter

router = APIRouter()

@router.get("/daily")
def get_daily_operations_report():
    """
    Mock metrics for the frontend operational dashboard representing ShopNow API trends.
    """
    return {
        "kpis": {
            "total_calls": 42050,
            "resolution_rate": "89.4%",
            "active_escalations": 3,
            "csat_score": 4.8
        },
        "intent_volume": [
            {"intent": "Order Status", "count": 18000},
            {"intent": "Return/Refund", "count": 12000},
            {"intent": "Delivery Complaint", "count": 6000},
            {"intent": "Payment Issue", "count": 4050},
            {"intent": "Product Query", "count": 2000}
        ],
        "sentiment_by_language": [
            {"language": "English", "positive": 75, "neutral": 20, "negative": 5},
            {"language": "Hindi", "positive": 60, "neutral": 30, "negative": 10},
            {"language": "Regional (Tamil)", "positive": 65, "neutral": 25, "negative": 10}
        ]
    }
