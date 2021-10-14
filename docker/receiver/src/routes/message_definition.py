from fastapi import APIRouter, Header
from .example_loader import load_example

route = APIRouter()


@route.get("/MessageDefinition")
def get_metadata(NHSD_Service: str = Header(...)):
    return load_example("message_definition/GET-success.json")
