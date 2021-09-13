import uvicorn

from fastapi import FastAPI
from datetime import datetime
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from enum import Enum


class Status(Enum):
    status_free = "free"
    status_busy = "busy"


app = FastAPI()


@app.exception_handler(RequestValidationError)
def validation_exception_handler(request, exc):
    return PlainTextResponse(str("something"), status_code=400)


@app.get("/Slot")
def Slot(
    healthcareService: str,
    status: Status,
    start: datetime,
    end: datetime,
    _include: str,
):
    return {"healthcareService": healthcareService}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
