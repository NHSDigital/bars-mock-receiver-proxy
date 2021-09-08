from flask import Blueprint

from responses.response_bank import responses

appointment = Blueprint('environments', __name__)


@appointment.route('/Appointment', methods=['GET'])
def get_appointments():
    return 'you hit env'


@appointment.route('/Appointment', methods=['POST'])
def create_appointment():
    return 'you post to env'


@appointment.route('/Appointment/<_id>', methods=['GET'])
def get_appointment(_id: int):
    return responses.success('Appointment')


@appointment.route('/Appointment/<_id>', methods=['PATCH'])
def patch_appointment(_id: int):
    return f'/PATCH {_id}'


@appointment.route('/Appointment/<_id>', methods=['PUT'])
def update_appointment(_id: int):
    return f'/PUT {_id}'


@appointment.route('/Appointment/<_id>', methods=['DELETE'])
def delete_appointment(_id: int):
    return f'/DELETE {_id}'
