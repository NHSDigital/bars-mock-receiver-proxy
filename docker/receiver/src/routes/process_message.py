<<<<<<< HEAD
from fastapi import APIRouter, Header
from .examples.example_loader import load_example


route = APIRouter()


@route.post("/$process-message")
def post_process_message(NHSD_ServiceIdentifier: str = Header(...)):
    return load_example("process_message/POST-success.json")
=======
from flask import Blueprint
from .examples.example_loader import load_example

process_message = Blueprint('process_message', __name__)


@process_message.route('/$process-message', methods=['POST'])
def create_process_message():
    return load_example('process_message/POST-success.json')
>>>>>>> c8f671a1d5384ee86e176929c305c9163eb09f19
