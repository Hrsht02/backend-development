# ============================================
# Topic 6: Nested Models in Pydantic
# ============================================

# A nested model means using one Pydantic model as a field
# inside another Pydantic model.
# It is useful when JSON data contains objects inside objects.
# Example: a Zoo has its own details and an Animal object.

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Inner Model: describes one animal.
class Animals(BaseModel):
    name: str
    type: str


# Outer Model: the animals field uses the Animals model.
# The request body must contain a nested JSON object matching this schema.
class Zoo(BaseModel):
    name: str
    location: str
    animals: Animals


# Example JSON:
# {
#   "name": "National Zoo",
#   "location": "Delhi",
#   "animals": {"name": "Lion", "type": "Mammal"}
# }
@app.post("/create-zoo")
def create_zoo(zoo: Zoo):
    return {
        "message": "Zoo data received",
        "zoo": zoo
    }


# Run: uvicorn 06_nested_models:app --reload
# Test at http://127.0.0.1:8000/docs
