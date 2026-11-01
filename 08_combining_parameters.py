# ============================================
# Topic 8: Path + Query + Request Body Combined
# ============================================

# One API endpoint can use different kinds of parameters:
#
# Path parameter:
#   Identifies a resource as part of the URL path.
# Query parameter:
#   Provides optional settings or filters after ? in the URL.
# Request body:
#   Sends structured data, commonly as JSON, to the API.
#
# In this example:
# - city_name is a path parameter.
# - notify is a query parameter.
# - city is a Pydantic request body.

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

cities = []


# Pydantic Model: defines the expected city request-body structure.
class City(BaseModel):
    name: str
    state: str
    area: int


# CREATE: POST receives city data in the JSON request body.
@app.post("/city")
def create_city(city: City):
    cities.append(city)
    return {
        "message": "City created successfully",
        "city": city
    }


# UPDATE using all three parameter types
# city_name comes from the URL path.
# notify is an optional query parameter; its default is False.
# city is received and validated from the JSON request body.
#
# Example URL: PUT /city/Patna?notify=true
# Example body: {"name": "Patna", "state": "Bihar", "area": 320}
@app.put("/city/{city_name}")
def update_city(city: City, city_name: str, notify: bool = False):
    for index, existing_city in enumerate(cities):
        if existing_city.name == city_name:
            cities[index] = city
            return {
                "message": "City updated successfully",
                "city": city,
                "notify": notify
            }

    return {
        "error": "City not found",
        "notify": notify
    }


# Run: uvicorn 08_combining_parameters:app --reload
# Test at http://127.0.0.1:8000/docs
