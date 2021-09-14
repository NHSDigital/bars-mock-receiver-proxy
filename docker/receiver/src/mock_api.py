from flask import Flask, Response
from routes.appointment import appointment
from routes.slots import slots
from routes.service_request import service_request
from routes.process_message import process_message
from routes.examples.example_loader import load_example

app = Flask(__name__)
app.register_blueprint(appointment)
app.register_blueprint(slots)
app.register_blueprint(service_request)
app.register_blueprint(process_message)


@app.route("/meta")
def meta():
    return Response(status=200)


@app.route("/_status")
def status():
    return load_example('status/_status.json')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
