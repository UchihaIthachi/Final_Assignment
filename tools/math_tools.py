from langchain_core.tools import tool

@tool
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

@tool
def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b

@tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

@tool
def divide(a: float, b: float) -> float:
    """Divide a by b. Raises an error if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

@tool
def modulus(a: float, b: float) -> float:
    """Return the modulus (remainder) of a divided by b."""
    return a % b

@tool
def power(a: float, b: float) -> float:
    """Return a raised to the power of b."""
    return a ** b

@tool
def sqrt(x: float) -> float:
    """Return the square root of x. Raises error if x is negative."""
    if x < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    return x ** 0.5

@tool
def abs_val(x: float) -> float:
    """Return the absolute value of x."""
    return abs(x)
