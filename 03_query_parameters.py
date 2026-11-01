# ============================================
# Topic 3: Query Parameters
# ============================================

# Query parameters are values passed after ? in a URL.
# They are commonly used for searching, filtering and pagination.
# Examples: /user?name=mohit and /products?price=1000
# Multiple query parameters are separated using &.

from fastapi import FastAPI

app = FastAPI()


# Basic Query Parameter
# price is not part of the route path, so FastAPI reads it from the query string.
@app.get("/price")
def get_price(price: int):
    return {"price": price}


# Optional Query Parameter
# None means the parameter is optional. If bike is not provided,
# its value will be None.
@app.get("/bike")
def get_bike(bike: str | None = None):
    return {"bike": bike}


# Default Value
# If color is not provided, FastAPI uses "red".
@app.get("/color")
def get_color(color: str = "red"):
    return {"color": color}


# Multiple Query Parameters
# We can accept more than one query parameter in a route.
# Use 0 as the default PIN value. 00000 is not a valid Python integer literal.
@app.get("/address")
def get_address(town: str | None = None, pin_code: int = 0):
    return {"town": town, "pin_code": pin_code}


# Run: uvicorn 03_query_parameters:app --reload
# Try: /price?price=1000
#      /bike
#      /color
#      /address?town=Patna&pin_code=800001
# Swagger UI: http://127.0.0.1:8000/docs
