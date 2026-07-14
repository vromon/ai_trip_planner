from app.schemas.trip_schema import TripSchema
def create_trip_plan(body:TripSchema):
    return{"status":"Your trip plan is ready!"}