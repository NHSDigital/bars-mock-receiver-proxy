from flask import Blueprint, request, Response
from .examples.example_loader import load_example

slots = Blueprint('slots', __name__)


@slots.route('/Slots', methods=['GET'])
def get_slots():
    status = 200
    if "healthcareService" not in request.args:
        status = 400
    if "status" not in request.args:
        status = 400
    if "start" not in request.args:
        status = 400
    if "end" not in request.args:
        status = 400
    if "_include" not in request.args:
        status = 400

    if status == 400:
        return Response(load_example('slots/GET-BadRequest.json'), status)
    return load_example('slots/GET-success.json')
