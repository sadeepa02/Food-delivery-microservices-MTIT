from fastapi import FastAPI
from routes.restaurant_routes import router
import uvicorn

app = FastAPI(title="Restaurant Service")

@app.get("/")
def home():
    return {"message": "Restaurant Service is running on port 8001"}

app.include_router(router, prefix="/restaurants", tags=["Restaurants"])

# 👇 Default run config
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=False)
