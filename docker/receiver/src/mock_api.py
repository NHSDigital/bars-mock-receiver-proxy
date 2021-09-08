from flask import Flask, Response

app = Flask(__name__)


@app.route("/meta")
def meta():
    return Response(status=200)


@app.route("/_status")
def status():
    return Response(status=200)


@app.route("/slots")
def slots():
    if "response-type" in request.headers:
        expected_response = request.headers["response-type"]
        return "401"
    return Response(status=200)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
