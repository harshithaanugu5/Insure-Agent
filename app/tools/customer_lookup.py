from __future__ import annotations


def lookup_customer_data(customer_id: str | None = None) -> dict:
    if customer_id:
        return {"customer_id": customer_id, "status": "found"}
    return {"customer_id": "demo-customer", "status": "demo"}
