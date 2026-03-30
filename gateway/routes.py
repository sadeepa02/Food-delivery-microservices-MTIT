from fastapi import APIRouter, Request, Response
from proxy import forward_request, SERVICES

router = APIRouter()

# ─── Restaurant Routes ────────────────────────────────────────────────────────
@router.api_route("/restaurants", methods=["GET", "POST"], tags=["🍽️ Restaurants"])
async def restaurants(request: Request):
    """Gateway → Restaurant Service"""
    return await forward_request(SERVICES["restaurants"], "/restaurants", request)

@router.api_route("/restaurants/{restaurant_id}", methods=["GET", "PUT", "DELETE"], tags=["🍽️ Restaurants"])
async def restaurant_by_id(restaurant_id: int, request: Request):
    """Gateway → Restaurant Service (by ID)"""
    return await forward_request(SERVICES["restaurants"], f"/restaurants/{restaurant_id}", request)

# ─── Menu Routes ─────────────────────────────────────────────────────────────
@router.api_route("/menu", methods=["GET", "POST"], tags=["📋 Menu"])
async def menu(request: Request):
    """Gateway → Menu Service"""
    return await forward_request(SERVICES["menu"], "/menu", request)

@router.api_route("/menu/{item_id}", methods=["GET", "PUT", "DELETE"], tags=["📋 Menu"])
async def menu_item(item_id: int, request: Request):
    """Gateway → Menu Service (by item ID)"""
    return await forward_request(SERVICES["menu"], f"/menu/{item_id}", request)

@router.api_route("/menu/restaurant/{restaurant_id}", methods=["GET"], tags=["📋 Menu"])
async def menu_by_restaurant(restaurant_id: int, request: Request):
    """Gateway → Menu Service (by restaurant)"""
    return await forward_request(SERVICES["menu"], f"/menu/restaurant/{restaurant_id}", request)

# ─── Order Routes ─────────────────────────────────────────────────────────────
@router.api_route("/orders", methods=["GET", "POST"], tags=["🛒 Orders"])
async def orders(request: Request):
    """Gateway → Order Service"""
    return await forward_request(SERVICES["orders"], "/orders", request)

@router.api_route("/orders/{order_id}", methods=["GET", "DELETE"], tags=["🛒 Orders"])
async def order_by_id(order_id: int, request: Request):
    """Gateway → Order Service (by ID)"""
    return await forward_request(SERVICES["orders"], f"/orders/{order_id}", request)

@router.api_route("/orders/{order_id}/status", methods=["PATCH"], tags=["🛒 Orders"])
async def order_status(order_id: int, request: Request):
    """Gateway → Order Service (update status)"""
    return await forward_request(SERVICES["orders"], f"/orders/{order_id}/status", request)

@router.api_route("/orders/restaurant/{restaurant_id}", methods=["GET"], tags=["🛒 Orders"])
async def orders_by_restaurant(restaurant_id: int, request: Request):
    """Gateway → Order Service (by restaurant)"""
    return await forward_request(SERVICES["orders"], f"/orders/restaurant/{restaurant_id}", request)

# ─── Delivery Routes ──────────────────────────────────────────────────────────
@router.api_route("/deliveries", methods=["GET", "POST"], tags=["🚴 Deliveries"])
async def deliveries(request: Request):
    """Gateway → Delivery Service"""
    return await forward_request(SERVICES["deliveries"], "/deliveries", request)

@router.api_route("/deliveries/{delivery_id}", methods=["GET", "DELETE"], tags=["🚴 Deliveries"])
async def delivery_by_id(delivery_id: int, request: Request):
    """Gateway → Delivery Service (by ID)"""
    return await forward_request(SERVICES["deliveries"], f"/deliveries/{delivery_id}", request)

@router.api_route("/deliveries/{delivery_id}/status", methods=["PATCH"], tags=["🚴 Deliveries"])
async def delivery_status(delivery_id: int, request: Request):
    """Gateway → Delivery Service (update status)"""
    return await forward_request(SERVICES["deliveries"], f"/deliveries/{delivery_id}/status", request)

@router.api_route("/deliveries/order/{order_id}", methods=["GET"], tags=["🚴 Deliveries"])
async def delivery_by_order(order_id: int, request: Request):
    """Gateway → Delivery Service (by order)"""
    return await forward_request(SERVICES["deliveries"], f"/deliveries/order/{order_id}", request)

# ─── Payment Routes ───────────────────────────────────────────────────────────
@router.api_route("/payments", methods=["GET", "POST"], tags=["💳 Payments"])
async def payments(request: Request):
    """Gateway → Payment Service"""
    return await forward_request(SERVICES["payments"], "/payments", request)

@router.api_route("/payments/{payment_id}", methods=["GET", "DELETE"], tags=["💳 Payments"])
async def payment_by_id(payment_id: int, request: Request):
    """Gateway → Payment Service (by ID)"""
    return await forward_request(SERVICES["payments"], f"/payments/{payment_id}", request)

@router.api_route("/payments/{payment_id}/status", methods=["PATCH"], tags=["💳 Payments"])
async def payment_status(payment_id: int, request: Request):
    """Gateway → Payment Service (update status)"""
    return await forward_request(SERVICES["payments"], f"/payments/{payment_id}/status", request)

@router.api_route("/payments/order/{order_id}", methods=["GET"], tags=["💳 Payments"])
async def payment_by_order(order_id: int, request: Request):
    """Gateway → Payment Service (by order)"""
    return await forward_request(SERVICES["payments"], f"/payments/order/{order_id}", request)
