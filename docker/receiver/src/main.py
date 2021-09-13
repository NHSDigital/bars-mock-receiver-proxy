import uvicorn
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from routes import slots


app = FastAPI()


@app.exception_handler(RequestValidationError)
def validation_exception_handler(request, exc):
    return PlainTextResponse(str("something"), status_code=400)


app.include_router(slots.route)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
