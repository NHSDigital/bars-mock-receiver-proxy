import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from routes import slots
from routes.examples.example_loader import load_example



app = FastAPI()


@app.exception_handler(RequestValidationError)
def validation_exception_handler(request, exc):
    response = load_example("bad-request.json")
    return PlainTextResponse(str(response), status_code=400)


app.include_router(slots.route)


@app.get("/_status")
def status():
    return load_example("_status.json")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
