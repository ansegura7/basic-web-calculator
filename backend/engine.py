async def calculate(value1: float, value2: float, operation: str) -> float:
    operation = operation.lower()

    if operation == "add":
        result = value1 + value2

    elif operation == "subtract":
        result = value1 - value2

    elif operation == "multiply":
        result = value1 * value2

    elif operation == "divide":
        if value2 == 0:
            raise ValueError("Division by zero is not allowed")
        result = value1 / value2

    else:
        raise ValueError("Invalid operation")

    return result
