from flask import Blueprint
from .examples.example_loader import load_example

process_message = Blueprint('process_message', __name__)


@process_message.route('/$process-message', methods=['POST'])
def create_process_message():
    return load_example('process_message/POST-success.json')
