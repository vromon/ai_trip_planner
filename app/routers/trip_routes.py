from app.services import trip_service
from fastapi import APIRouter
from app.schemas.trip_schema import TripSchema
trip_router=APIRouter(prefix="/trip")
@trip_router.post("/generate")
def create_trip_plan(trip_request:TripSchema):
    return trip_service.create_trip_plan(trip_request)