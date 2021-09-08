from flask import Flask, request, Response

app = Flask(__name__)


@app.route("/meta")
def meta():
    return Response(status=200)


@app.route("/_status")
def status():
    return Response(status=200)


@app.route("/slots")
def slots():
    if "a-test" in request.body:
        # expected_response = request.headers["response-type"]
        return Response(status=200)
    return Response(status=401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
