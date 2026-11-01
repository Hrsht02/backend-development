# ============================================
# Topic 9: Response Models & Hiding Sensitive Data
# ============================================

# A response model defines the structure of data an API endpoint
# is allowed to return.
# It helps keep responses consistent and prevents accidental exposure
# of fields that should remain private.
#
# Email contains a password, but UserResponse does not.
# FastAPI filters the returned data according to response_model.

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Full Model: includes the sensitive password field.
class Email(BaseModel):
    email: str
    subject: str
    password: str


# Public Response Model: intentionally excludes the password.
class UserResponse(BaseModel):
    email: str
    subject: str


# response_model tells FastAPI to validate and filter the returned data.
# This is a POST endpoint because Email is received as a request body.
@app.post("/email", response_model=UserResponse)
def get_email(email: Email):
    return {
        "email": email.email,
        "subject": email.subject,
        "password": email.password
    }


# Even though the function returns a password, FastAPI removes it
# from the final response because UserResponse has no password field.
# Never return real passwords or store them as plain text.
#
# Run: uvicorn 09_response_models:app --reload
# Test at http://127.0.0.1:8000/docs
