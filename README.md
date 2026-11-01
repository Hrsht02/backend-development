# Backend Development with FastAPI

A topic-wise collection of my FastAPI practice code and beginner-friendly notes. Each Python file is independent and has its own FastAPI application instance.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Hrsht02/backend-development.git
   cd backend-development
   ```

2. Create and activate a virtual environment:

   **Windows (PowerShell):**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

   **macOS / Linux:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Topics and practice files

| # | File | Concepts |
|---|---|---|
| 01 | [01_basic_routes.py](01_basic_routes.py) | FastAPI app, GET requests, routes and Swagger UI |
| 02 | [02_path_parameters.py](02_path_parameters.py) | Dynamic routes, path parameters and type hints |
| 03 | [03_query_parameters.py](03_query_parameters.py) | Query parameters, optional values, defaults and multiple parameters |
| 04 | [04_request_body_post.py](04_request_body_post.py) | POST requests, JSON request bodies and dictionaries |
| 05 | [05_pydantic_models.py](05_pydantic_models.py) | Pydantic BaseModel, schemas, validation and serialization |
| 06 | [06_nested_models.py](06_nested_models.py) | Nested Pydantic models |
| 07 | [07_crud_operations.py](07_crud_operations.py) | Create, Read, Update and Delete with a To-Do API |
| 08 | [08_combining_parameters.py](08_combining_parameters.py) | Path parameters, query parameters and request bodies together |
| 09 | [09_response_models.py](09_response_models.py) | Response models and hiding sensitive fields |
| 10 | [10_status_codes.py](10_status_codes.py) | HTTP status codes and error handling |

## Running a topic

Run one file at a time from the repository root. For example:

```bash
uvicorn 01_basic_routes:app --reload
```

Replace `01_basic_routes` with the filename (without `.py`) of the topic you want to practise.

Open these URLs while the server is running:

- API: http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

**Important:** Only run one practice file at a time because each file defines its own `app` instance and commonly uses the same local server port.

## Notes

- These examples are for learning. The To-Do and City examples store data in Python lists, so the data resets when the server restarts.
- GET requests can be opened directly in a browser. To test POST, PUT and DELETE requests, use Swagger UI, an API client, or `curl`.
- The examples use in-memory data and do not yet include a database or authentication.
