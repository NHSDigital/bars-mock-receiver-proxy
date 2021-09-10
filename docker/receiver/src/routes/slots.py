from flask import Blueprint
from .examples.example_loader import load_example

slots = Blueprint('environments', __name__)


@slots.route('/Slots', methods=['GET'])
def get_slots():
    return load_example('slots/GET-success.json')

