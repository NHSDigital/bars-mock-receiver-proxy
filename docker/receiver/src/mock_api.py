from flask import Flask, request, Response

app = Flask(__name__)


@app.route("/meta")
def meta():
    return Response(status=200)


@app.route("/_status")
def status():
    return Response(status=200)


@app.route("/Slot")
def slots():
    return Response(status=200)
    # status = 200
    # if "healthcareService" not in request.args:
    #     status = 400
    # if "status" not in request.args:
    #     status = 400
    # if "start" not in request.args:
    #     status = 400
    # if "end" not in request.args:
    #     status = 400
    # if "_include" not in request.args:
    #     status = 400
    #
    # if status == 400:
    #     return Response('Bad Request', status=status)
    # else:
    #     return Response('Success', status=status)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
