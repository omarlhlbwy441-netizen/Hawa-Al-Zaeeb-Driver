from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from services.api_gateway.routers import orders

app = FastAPI(title="Wolf Driver API", description="نظام إدارة الطلبات الذكي")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(orders.router)

@app.get("/")
def root():
    return {"status": "online", "system": "design-framework"}