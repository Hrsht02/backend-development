# ============================================
# Topic 1: Introduction to FastAPI & Basic Routes
# ============================================

# An API (Application Programming Interface) allows
# two applications to communicate and exchange data.
#
# FastAPI is a Python framework used to build APIs.
# It provides automatic documentation, request validation
# and support for asynchronous endpoints.

from fastapi import FastAPI

# Creating a FastAPI application instance.
# We use this object to define our API routes.
app = FastAPI()


# Home Route
# GET request is used to fetch or retrieve data.
# "/" represents the root or home endpoint.
# When a client visits "/", this function gets executed.

@app.get("/")
def home():
    return {"message": "Hello, world!"}


# About Route
# We can create multiple routes in one FastAPI application.
# One function is connected to one route in these examples.

@app.get("/about")
def about():
    return {"message": "This is about page."}


# Users Route
# A Python list and dictionary are automatically converted
# into a JSON response by FastAPI.

@app.get("/users")
def user():
    return {
        "users": ["Mohit", "Rohit"]
    }


# ============================================
# Running the Application
# ============================================
# Run in the terminal:
# uvicorn 01_basic_routes:app --reload
#
# Open:
# http://127.0.0.1:8000/
# http://127.0.0.1:8000/about
# http://127.0.0.1:8000/users
# Swagger UI: http://127.0.0.1:8000/docs
