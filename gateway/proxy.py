import httpx
from fastapi import Request, Response, HTTPException

SERVICES = {
    "restaurants": "http://localhost:8001",
    "menu": "http://localhost:8002",
    "orders": "http://localhost:8003",
    "deliveries": "http://localhost:8004",
    "payments": "http://localhost:8005",
}

async def forward_request(service_url: str, path: str, request: Request) -> Response:
    """Forward an incoming request to the appropriate microservice."""
    url = f"{service_url}{path}"
    
    # Read request body
    body = await request.body()
    
    # Build headers (exclude host to avoid conflicts)
    headers = {
        key: value
        for key, value in request.headers.items()
        if key.lower() not in ("host", "content-length")
    }
    
    async with httpx.AsyncClient(timeout=10.0, follow_redirects=True) as client:
        try:
            response = await client.request(
                method=request.method,
                url=url,
                headers=headers,
                content=body,
                params=dict(request.query_params),
            )
            return Response(
                content=response.content,
                status_code=response.status_code,
                headers=dict(response.headers),
                media_type=response.headers.get("content-type", "application/json"),
            )
        except httpx.ConnectError:
            raise HTTPException(
                status_code=503,
                detail=f"Service unavailable: Could not connect to {service_url}. Ensure the service is running."
            )
        except httpx.TimeoutException:
            raise HTTPException(
                status_code=504,
                detail=f"Gateway timeout: The upstream service at {service_url} did not respond in time."
            )
