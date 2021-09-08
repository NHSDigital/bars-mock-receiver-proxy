from flask import Flask, Response
from routes.appointment import appointment

import os
import sys

sys.path.append(os.getcwd())
app = Flask(__name__)
app.register_blueprint(appointment)


@app.route("/meta")
def meta():
    return Response(status=200)


@app.route("/_status")
def status():
    return Response(status=200)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
