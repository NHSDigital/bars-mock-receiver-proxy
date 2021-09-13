from fastapi import APIRouter
from enum import Enum
from datetime import datetime


route = APIRouter()


class Status(Enum):
    status_free = "free"
    status_busy = "busy"


@route.get("/Slot")
def Slot(
    healthcareService: str,
    status: Status,
    start: datetime,
    end: datetime,
    _include: str,
):
    return {"healthcareService": healthcareService}
