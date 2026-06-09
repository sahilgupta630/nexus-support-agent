from typing import Optional

MOCK_ORDERS = {
    "ORD123": {
        "status": "Shipped",
        "delivery_date": "2026-06-12",
        "items": ["Wireless Earbuds"],
        "user": "Alice"
    },
    "ORD456": {
        "status": "Processing",
        "delivery_date": "2026-06-15",
        "items": ["Mechanical Keyboard"],
        "user": "Bob"
    },
    "ORD789": {
        "status": "Delivered",
        "delivery_date": "2026-06-01",
        "items": ["Gaming Mouse"],
        "user": "Charlie"
    }
}

def get_order_details(order_id: str) -> Optional[dict]:
    # Mock database lookup
    o_id = order_id.upper().strip()
    return MOCK_ORDERS.get(o_id, None)

def initiate_return(order_id: str, reason: str) -> dict:
    # Mocks return initiation
    o_id = order_id.upper().strip()
    if o_id in MOCK_ORDERS:
        return {"success": True, "message": f"Return initiated for {o_id} due to '{reason}'."}
    return {"success": False, "message": "Order not found."}
