from flask import Blueprint, Response
from .examples.example_loader import load_example

service_request = Blueprint('service_request', __name__)


@service_request.route('/ServiceRequest', methods=['GET'])
def get_referrals():
    return load_example('service_request/GET-success.json')


@service_request.route('/ServiceRequest', methods=['POST'])
def create_referrals():
    body = ''

    return Response(body, status=201)


@service_request.route('/ServiceRequest/<_id>', methods=['GET'])
def get_referral(_id: str):
    return load_example('service_request/id/GET-success.json')


@service_request.route('/ServiceRequest/<_id>', methods=['PUT'])
def put_referral(_id: str):
    return load_example('service_request/id/PUT-success.json')


@service_request.route('/ServiceRequest/<_id>', methods=['PATCH'])
def patch_referral(_id: str):
    return load_example('service_request/id/PATCH-success.json')


@service_request.route('/ServiceRequest/<_id>', methods=['DELETE'])
def delete_referral(_id: str):
    return ''
