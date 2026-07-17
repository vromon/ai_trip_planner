from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
def register_exception_handlers(app:FastAPI):
    @app.exception_handler(Exception)
    def global_exception_handler(request:Request,exc:Exception):
        print(f"server error:{exc}")
        return JSONResponse(
            status_code=500,
            content={
                "success":False,
                "message":"Internal Server Error"
            }
        )
