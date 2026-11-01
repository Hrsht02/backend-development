# ============================================
# Topic 10: HTTP Status Codes & Error Handling
# ============================================

# HTTP status codes tell the client what happened after
# the server processed a request.
#
# Common status codes:
# 200 - OK: request was successful.
# 201 - Created: a resource was successfully created.
# 400 - Bad Request: the request is invalid.
# 404 - Not Found: the requested resource does not exist.
# 500 - Internal Server Error: an unexpected server error occurred.
#
# FastAPI normally returns 200 for a successful endpoint.
# We can set a different success status code using status_code.
# HTTPException is used to return an HTTP error response.

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()


class Product(BaseModel):
    id: int
    name: str
    price: float


products = []


# 201 Created
# status_code sets the HTTP status code for a successful response.
@app.post("/products", status_code=status.HTTP_201_CREATED)
def create_product(product: Product):
    if any(existing_product.id == product.id for existing_product in products):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Product ID already exists"
        )

    products.append(product)
    return {
        "message": "Product created successfully",
        "product": product
    }


# 200 OK: a successful GET request returns the product list.
@app.get("/products", status_code=status.HTTP_200_OK)
def get_products():
    return products


# 404 Not Found
# HTTPException stops normal execution and sends an HTTP error response.
@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Product not found"
    )


# Note:
# FastAPI also performs automatic request validation.
# Invalid request bodies or typed parameters normally produce
# a 422 Unprocessable Entity response.
#
# Run: uvicorn 10_status_codes:app --reload
# Test at http://127.0.0.1:8000/docs
