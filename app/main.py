from fastapi import FastAPI
app=FastAPI(title="AI Trip Planner Server")
@app.get("/")
def home():
    return{"status":"AI Trip Planner is Running"}