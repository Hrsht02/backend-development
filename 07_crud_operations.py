# ============================================
# Topic 7: CRUD Operations - To-Do API
# ============================================

# CRUD stands for:
# Create -> POST request
# Read   -> GET request
# Update -> PUT request
# Delete -> DELETE request
#
# We will practise CRUD using a To-Do list.
# todos is a normal Python list (in-memory storage).
# Data will be lost when the application restarts.

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []


# Pydantic Model
# Every To-Do item has an integer id, a task and a status.
class Todo(BaseModel):
    id: int
    task: str
    status: bool


# CREATE
# POST is used to create a new To-Do item.
@app.post("/todos")
def create_todo(todo: Todo):
    if any(existing_todo.id == todo.id for existing_todo in todos):
        return {"error": "Todo ID already exists"}

    todos.append(todo)
    return {
        "message": "Todo created successfully",
        "todo": todo
    }


# READ - Get all To-Do items
@app.get("/todos")
def get_todos():
    return todos


# READ - Get one To-Do item using a path parameter
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo

    return {"error": "Todo not found"}


# UPDATE
# PUT replaces/updates an existing resource.
# enumerate() gives both the list index and the item.
# We use the index to replace the matching item.
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            if updated_todo.id != todo_id:
                return {"error": "Todo ID in URL and body must match"}

            todos[index] = updated_todo
            return {
                "message": "Todo updated successfully",
                "todo": updated_todo
            }

    # This return must be outside the for-loop.
    # Otherwise, the function stops after checking only the first item.
    return {"error": "Todo not found"}


# DELETE
# del removes an element from a list using its index.
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            del todos[index]
            return {"message": "Todo deleted successfully"}

    return {"error": "Todo not found"}


# Run: uvicorn 07_crud_operations:app --reload
# Test POST, GET, PUT and DELETE at http://127.0.0.1:8000/docs
