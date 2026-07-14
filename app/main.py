from fastapi import FastAPI
from app.routers.trip_routes import trip_router
app=FastAPI(title="AI Trip Planner Server")
@app.get("/")
def home():
    return{"status":"AI Trip Planner is Running"}
app.include_router(trip_router)