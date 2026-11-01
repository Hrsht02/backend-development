# ============================================
# Topic 2: Path Parameters
# ============================================

# Path parameters are values included directly in the URL path.
# They help us identify a particular resource, such as a user or product.
# Example: /users/10 or /games/cricket
# The value inside { } is dynamic and is passed to the function.

from fastapi import FastAPI

app = FastAPI()


# Dynamic Route
# user_id is taken from the URL. Without a type hint, it is a string.
@app.get("/get_user/{user_id}")
def get_user(user_id):
    return {"user_id": user_id}


# Path Parameter with a Data Type
# :str tells FastAPI that game_name should be a string.
@app.get("/games/{game_name}")
def get_game(game_name: str):
    return {"game_name": game_name}


# Integer Path Parameter
# FastAPI validates that product_id is an integer.
@app.get("/products/{product_id}")
def get_product(product_id: int):
    return {"product_id": product_id}


# Run: uvicorn 02_path_parameters:app --reload
# Try: /get_user/101, /games/cricket, /products/25
# Swagger UI: http://127.0.0.1:8000/docs
