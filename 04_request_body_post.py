# ============================================
# Topic 4: Request Body & POST Requests
# ============================================

# GET is generally used to retrieve data.
# POST is generally used to submit data or create a resource.
# A request body contains data sent by the client to the server.
# JSON is a common format for sending request-body data.
#
# GET requests can be opened directly in a browser.
# To test POST, PUT and DELETE, use Swagger UI (/docs) or an API client.

from fastapi import FastAPI

app = FastAPI()


# POST with Simple Parameters
# These simple function parameters are query parameters,
# not a JSON request body.
# Example: POST /create_user?name=Mohit&age=20
@app.post("/create_user")
def create_user(name: str | None = None, age: int | None = None):
    return {"name": name, "age": age}


# JSON Request Body using dict
# A dict parameter is interpreted as a JSON request body.
# Example JSON:
# {"name": "Virat", "role": "Batsman", "team": "India"}
#
# Issue: a plain dictionary does not define a strict schema.
# We do not get the same field-level validation as a Pydantic model.
@app.post("/cricketer")
def cricketer_detail(detail: dict):
    return {
        "message": "Player Detail",
        "detail": detail
    }


# Run: uvicorn 04_request_body_post:app --reload
# Test the POST endpoints at http://127.0.0.1:8000/docs
