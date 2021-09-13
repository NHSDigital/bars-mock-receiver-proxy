from fastapi import APIRouter
from enum import Enum
from datetime import datetime
from .examples.example_loader import load_example


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
    return load_example("slots/GET-success.json")
