from flask import Blueprint, Request, Response
from .examples.example_loader import load_example

slots = Blueprint('slots', __name__)


@slots.route('/Slots', methods=['GET'])
def get_slots():
    if "start" not in Request.args:
        status = 400

    if status == 400:
        return Response('Bad Request', status)
    return load_example('slots/GET-success.json')
