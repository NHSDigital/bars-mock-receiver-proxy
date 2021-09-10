from flask import Blueprint, Response
from .examples.example_loader import load_example

appointment = Blueprint('environments', __name__)


@appointment.route('/Appointment', methods=['GET'])
def get_appointments():
    return load_example('appointment/GET-success.json')


@appointment.route('/Appointment', methods=['POST'])
def create_appointment():
    body = load_example('appointment/POST-success.txt')
    return Response(body, status=201)


@appointment.route('/Appointment/<_id>', methods=['GET'])
def get_appointment(_id: str):
    return load_example('appointment/id/GET-success.json')


@appointment.route('/Appointment/<_id>', methods=['PATCH'])
def patch_appointment(_id: str):
    return ''


@appointment.route('/Appointment/<_id>', methods=['PUT'])
def update_appointment(_id: str):
    return ''


@appointment.route('/Appointment/<_id>', methods=['DELETE'])
def delete_appointment(_id: str):
    return ''
