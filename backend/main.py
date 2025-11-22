from enum import Enum
from pydantic import BaseModel

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from engine import calculate
from data_layer import initialize_db, get_all_operations

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Operation(str, Enum):
    add = "add"
    subtract = "subtract"
    multiply = "multiply"
    divide = "divide"


class OperationRequest(BaseModel):
    value1: float
    value2: float
    operation: Operation


@app.on_event("startup")
def startup_event():
    initialize_db()


@app.post("/calculate")
async def calculate_endpoint(request: OperationRequest):
    value1 = request.value1
    value2 = request.value2
    operation = request.operation

    try:
        result = await calculate(value1, value2, operation)
        return {"result": result}

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


@app.get("/history")
def history():
    operations = get_all_operations()
    return {"operations": operations}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
