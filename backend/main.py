from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class OperationRequest(BaseModel):
    value1: float
    value2: float
    operation: str


@app.post("/calculate")
def calculate(request: OperationRequest):
    value1 = request.value1
    value2 = request.value2
    operation = request.operation

    if operation == "add":
        result = value1 + value2
    elif operation == "subtract":
        result = value1 - value2
    elif operation == "multiply":
        result = value1 * value2
    elif operation == "divide":
        if value2 == 0:
            raise HTTPException(
                status_code=400, detail="Division by zero is not allowed"
            )
        result = value1 / value2
    else:
        raise HTTPException(status_code=400, detail="Invalid operation")

    return {"result": result}
