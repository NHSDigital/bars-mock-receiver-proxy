from flask import Blueprint, request, Response
from .examples.example_loader import load_example
from datetime import datetime


slots = Blueprint('slots', __name__)


@slots.route('/Slots', methods=['GET'])
def get_slots():
    if "healthcareService" in request.args:
        # Validate the healtcareService value against the spec example value...
        if request.args.get("healtcareService") != "09a01679-2564-0fb4-5129-aecc81ea2706":
            entity_not_found = True
    else:
        ilegal_input_operation = True

    if "status" in request.args:
        # Validate status value against the spec example values...
        if request.args.get("status") != "free" or request.args.get("status") != "busy":
            ilegal_input_operation = True
    else:
        ilegal_input_operation = True

    if "start" not in request.args:
        ilegal_input_operation = True
    if "end" not in request.args:
        ilegal_input_operation = True
    if "_include" not in request.args:
        ilegal_input_operation = True

    if ilegal_input_operation:
        return Response(load_example('slots/GET-BadRequest.json'), 400)

    if entity_not_found:
        return Response(load_example('slots/GET-BadRequest.json'), 403)

    return load_example('slots/GET-success.json')
