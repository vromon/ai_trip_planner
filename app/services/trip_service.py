from app.schemas.trip_schema import TripSchema
from app.ai.chains.trip_chain import invoke_chain
def create_trip_plan(trip_request:TripSchema):
    return invoke_chain(trip_request.user_query)
