from typing import Any, Dict

from fastapi import APIRouter, Body, Request

from proxy import SERVICES, forward_request

router = APIRouter()
JsonBody = Dict[str, Any]


@router.get("/restaurants", tags=["Restaurants"])
async def get_restaurants(request: Request):
    return await forward_request(SERVICES["restaurants"], "/restaurants", request)


@router.post("/restaurants", tags=["Restaurants"])
async def create_restaurant(request: Request, payload: JsonBody = Body(...)):
    return await forward_request(SERVICES["restaurants"], "/restaurants", request)


@router.get("/restaurants/{restaurant_id}", tags=["Restaurants"])
async def get_restaurant(restaurant_id: str, request: Request):
    return await forward_request(SERVICES["restaurants"], f"/restaurants/{restaurant_id}", request)


@router.put("/restaurants/{restaurant_id}", tags=["Restaurants"])
async def update_restaurant(restaurant_id: str, request: Request, payload: JsonBody = Body(...)):
    return await forward_request(SERVICES["restaurants"], f"/restaurants/{restaurant_id}", request)


@router.delete("/restaurants/{restaurant_id}", tags=["Restaurants"])
async def delete_restaurant(restaurant_id: str, request: Request):
    return await forward_request(SERVICES["restaurants"], f"/restaurants/{restaurant_id}", request)


@router.get("/menu", tags=["Menu"])
async def get_menu(request: Request):
    return await forward_request(SERVICES["menu"], "/menu", request)


@router.post("/menu", tags=["Menu"])
async def create_menu_item(request: Request, payload: JsonBody = Body(...)):
    return await forward_request(SERVICES["menu"], "/menu", request)


@router.get("/menu/{item_id}", tags=["Menu"])
async def get_menu_item(item_id: int, request: Request):
    return await forward_request(SERVICES["menu"], f"/menu/{item_id}", request)


@router.put("/menu/{item_id}", tags=["Menu"])
async def update_menu_item(item_id: int, request: Request, payload: JsonBody = Body(...)):
    return await forward_request(SERVICES["menu"], f"/menu/{item_id}", request)


@router.delete("/menu/{item_id}", tags=["Menu"])
async def delete_menu_item(item_id: int, request: Request):
    return await forward_request(SERVICES["menu"], f"/menu/{item_id}", request)


@router.get("/menu/restaurant/{restaurant_id}", tags=["Menu"])
async def get_menu_by_restaurant(restaurant_id: int, request: Request):
    return await forward_request(SERVICES["menu"], f"/menu/restaurant/{restaurant_id}", request)


@router.get("/orders", tags=["Orders"])
async def get_orders(request: Request):
    return await forward_request(SERVICES["orders"], "/orders", request)


@router.post("/orders", tags=["Orders"])
async def create_order(request: Request, payload: JsonBody = Body(...)):
    return await forward_request(SERVICES["orders"], "/orders", request)


@router.get("/orders/{order_id}", tags=["Orders"])
async def get_order(order_id: int, request: Request):
    return await forward_request(SERVICES["orders"], f"/orders/{order_id}", request)


@router.delete("/orders/{order_id}", tags=["Orders"])
async def delete_order(order_id: int, request: Request):
    return await forward_request(SERVICES["orders"], f"/orders/{order_id}", request)


@router.patch("/orders/{order_id}/status", tags=["Orders"])
async def update_order_status(order_id: int, request: Request, payload: JsonBody = Body(...)):
    return await forward_request(SERVICES["orders"], f"/orders/{order_id}/status", request)


@router.get("/orders/restaurant/{restaurant_id}", tags=["Orders"])
async def get_orders_by_restaurant(restaurant_id: int, request: Request):
    return await forward_request(SERVICES["orders"], f"/orders/restaurant/{restaurant_id}", request)


@router.get("/deliveries", tags=["Deliveries"])
async def get_deliveries(request: Request):
    return await forward_request(SERVICES["deliveries"], "/deliveries", request)


@router.post("/deliveries", tags=["Deliveries"])
async def create_delivery(request: Request, payload: JsonBody = Body(...)):
    return await forward_request(SERVICES["deliveries"], "/deliveries", request)


@router.get("/deliveries/{delivery_id}", tags=["Deliveries"])
async def get_delivery(delivery_id: int, request: Request):
    return await forward_request(SERVICES["deliveries"], f"/deliveries/{delivery_id}", request)


@router.delete("/deliveries/{delivery_id}", tags=["Deliveries"])
async def delete_delivery(delivery_id: int, request: Request):
    return await forward_request(SERVICES["deliveries"], f"/deliveries/{delivery_id}", request)


@router.patch("/deliveries/{delivery_id}/status", tags=["Deliveries"])
async def update_delivery_status(delivery_id: int, request: Request, payload: JsonBody = Body(...)):
    return await forward_request(SERVICES["deliveries"], f"/deliveries/{delivery_id}/status", request)


@router.get("/deliveries/order/{order_id}", tags=["Deliveries"])
async def get_delivery_by_order(order_id: int, request: Request):
    return await forward_request(SERVICES["deliveries"], f"/deliveries/order/{order_id}", request)


@router.get("/payments", tags=["Payments"])
async def get_payments(request: Request):
    return await forward_request(SERVICES["payments"], "/payments", request)


@router.post("/payments", tags=["Payments"])
async def create_payment(request: Request, payload: JsonBody = Body(...)):
    return await forward_request(SERVICES["payments"], "/payments", request)


@router.get("/payments/{payment_id}", tags=["Payments"])
async def get_payment(payment_id: int, request: Request):
    return await forward_request(SERVICES["payments"], f"/payments/{payment_id}", request)


@router.delete("/payments/{payment_id}", tags=["Payments"])
async def delete_payment(payment_id: int, request: Request):
    return await forward_request(SERVICES["payments"], f"/payments/{payment_id}", request)


@router.patch("/payments/{payment_id}/status", tags=["Payments"])
async def update_payment_status(payment_id: int, request: Request, payload: JsonBody = Body(...)):
    return await forward_request(SERVICES["payments"], f"/payments/{payment_id}/status", request)


@router.get("/payments/order/{order_id}", tags=["Payments"])
async def get_payment_by_order(order_id: int, request: Request):
    return await forward_request(SERVICES["payments"], f"/payments/order/{order_id}", request)
