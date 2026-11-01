# ============================================
# Topic 5: Data Validation with Pydantic Models
# ============================================

# Pydantic is used for data validation and serialization.
# It checks incoming data against the fields and types defined in a model.
#
# A Pydantic model is a Python class that inherits from BaseModel.
# Models define schemas for request and response data.
# Benefits: expected data structure, validation, useful errors and API docs.

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Pydantic Model
# name should be a string and role should be an integer.
# Both fields are required because no default values are given.
class User(BaseModel):
    name: str
    role: int


# FastAPI reads the JSON request body and validates it using User.
# Example JSON: {"name": "Mohit", "role": 2}
@app.post("/cricketer")
def footballer_detail(detail: User):
    return {
        "message": "Player Detail",
        "detail": detail
    }


# Another Pydantic Model
# contact is an integer in this beginner example.
# In real applications, phone numbers are often strings so that
# leading zeros and a + country code are preserved.
class Singer(BaseModel):
    name: str
    age: int
    contact: int


@app.post("/create-singer")
def create_singer(singer: Singer):
    return {
        "message": "Singer data received",
        "singer": singer
    }


# Interview: Dictionary vs Pydantic
#
# A dictionary is a general-purpose Python data structure. It can hold
# different values and does not enforce a predefined schema by itself.
# A Pydantic model defines expected fields and validation rules.
# FastAPI uses it to validate request data and serialize model data.
#
# Run: uvicorn 05_pydantic_models:app --reload
# Test at http://127.0.0.1:8000/docs
