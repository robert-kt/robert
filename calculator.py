"""Simple command-line calculator app."""

from typing import Union

Number = Union[int, float]


def calculate(a: Number, b: Number, operation: str) -> Number:
    """Perform a calculation between two numbers.

    Parameters:
        a: First number.
        b: Second number.
        operation: One of '+', '-', '*', '/' representing the arithmetic operation.

    Returns:
        The result of the arithmetic operation.

    Raises:
        ValueError: If the operation is unsupported or division by zero is attempted.
    """
    if operation == '+':
        return a + b
    if operation == '-':
        return a - b
    if operation == '*':
        return a * b
    if operation == '/':
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    raise ValueError(f"Unsupported operation: {operation}")


def main() -> None:
    """Run the calculator interactively from the command line."""
    try:
        a = float(input("Enter first number: "))
        operation = input("Enter operation (+, -, *, /): ")
        b = float(input("Enter second number: "))
        result = calculate(a, b, operation)
        print(f"Result: {result}")
    except ValueError as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()
