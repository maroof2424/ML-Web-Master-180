def add(x: float, y: float) -> float:
    """
    Returns the sum of x and y.
    """
    return x + y

def subtract(x: float, y: float) -> float:
    """
    Returns the result of subtracting y from x.
    """
    return x - y

def divide(x: float, y: float) -> float:
    """
    Divides x by y. Raises ZeroDivisionError if y is 0.
    """
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y

def multiply(x: float, y: float) -> float:
    """
    Returns the product of x and y.
    """
    return x * y
