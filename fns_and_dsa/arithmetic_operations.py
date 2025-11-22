def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform a basic arithmetic operation on num1 and num2.

    operation: one of 'add', 'subtract', 'multiply', 'divide'
    Returns:
      - a float result for successful operations
      - the string "Error: Division by zero" if dividing by zero
      - the string "Error: Invalid operation" for unknown operations
    """
    op = operation.strip().lower()

    if op == "add":
        return num1 + num2
    elif op == "subtract":
        return num1 - num2
    elif op == "multiply":
        return num1 * num2
    elif op == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"