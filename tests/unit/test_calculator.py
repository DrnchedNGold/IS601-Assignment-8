# tests/unit/test_calculator.py

import pytest  # Import the pytest framework for writing and running tests
from typing import Union  # Import Union for type hinting multiple possible types
from app.operations import add, subtract, multiply, divide  # Import the calculator functions from the operations module

# Define a type alias for numbers that can be either int or float
Number = Union[int, float]


# ---------------------------------------------
# Unit Tests for the 'add' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),           # Test adding two positive integers
        (-2, -3, -5),        # Test adding two negative integers
        (2.5, 3.5, 6.0),     # Test adding two positive floats
        (-2.5, 3.5, 1.0),    # Test adding a negative float and a positive float
        (0, 0, 0),            # Test adding zeros
        (1000000, 2000000, 3000000),  # Test adding large numbers
        (-1000000, -2000000, -3000000),  # Test adding large negative numbers
        (0.1, 0.2, 0.3),      # Test adding small positive floats
        (-0.1, -0.2, -0.3),   # Test adding small negative floats
        (1e10, 2e10, 3e10),   # Test adding very large numbers in scientific notation
        (1e-10, 2e-10, 3e-10), # Test adding very small numbers in scientific notation
        (float('inf'), 1, float('inf')),  # Test adding infinity
        (-float('inf'), 1, -float('inf')), # Test adding negative infinity
        (0.123456789, 0.987654321, 1.11111111), # Test floating point precision
    ],
    ids=[
        "add_two_positive_integers",
        "add_two_negative_integers",
        "add_two_positive_floats",
        "add_negative_and_positive_float",
        "add_zeros",
        "add_large_positive_numbers",
        "add_large_negative_numbers",
        "add_small_positive_floats",
        "add_small_negative_floats",
        "add_scientific_notation_large",
        "add_scientific_notation_small",
        "add_positive_infinity",
        "add_negative_infinity",
        "add_floating_point_precision",
    ]
)
def test_add(a: Number, b: Number, expected: Number) -> None:
    """
    Test the 'add' function with various combinations of integers and floats.

    This parameterized test verifies that the 'add' function correctly adds two numbers,
    whether they are positive, negative, integers, or floats. By using parameterization,
    we can efficiently test multiple scenarios without redundant code.

    Parameters:
    - a (Number): The first number to add.
    - b (Number): The second number to add.
    - expected (Number): The expected result of the addition.

    Steps:
    1. Call the 'add' function with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    Example:
    >>> test_add(2, 3, 5)
    >>> test_add(-2, -3, -5)
    """
    # Call the 'add' function with the provided arguments
    result = add(a, b)
    
    # For floating point operations that might have precision issues, use pytest.approx
    if isinstance(a, float) or isinstance(b, float):
        assert result == pytest.approx(expected, rel=1e-9), f"Expected add({a}, {b}) to be {expected}, but got {result}"
    else:
        assert result == expected, f"Expected add({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Unit Tests for the 'subtract' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),           # Test subtracting a smaller positive integer from a larger one
        (-5, -3, -2),        # Test subtracting a negative integer from another negative integer
        (5.5, 2.5, 3.0),     # Test subtracting two positive floats
        (-5.5, -2.5, -3.0),  # Test subtracting two negative floats
        (0, 0, 0),            # Test subtracting zeros
        (1000000, 500000, 500000),  # Test subtracting large numbers
        (-1000000, -500000, -500000),  # Test subtracting large negative numbers
        (10, 15, -5),         # Test subtracting larger from smaller (negative result)
        (3.7, 1.2, 2.5),      # Test subtracting small positive floats
        (-3.7, -1.2, -2.5),   # Test subtracting small negative floats
        (1e10, 5e9, 5e9),     # Test subtracting very large numbers in scientific notation
        (1e-5, 5e-6, 5e-6),   # Test subtracting very small numbers in scientific notation
        (float('inf'), 1, float('inf')),  # Test subtracting from positive infinity
        (-float('inf'), 1, -float('inf')), # Test subtracting from negative infinity
        (5.123456789, 2.123456789, 3.0), # Test floating point precision
        (0, 5, -5),           # Test subtracting positive from zero
        (5, 0, 5),            # Test subtracting zero from positive
    ],
    ids=[
        "subtract_two_positive_integers",
        "subtract_two_negative_integers",
        "subtract_two_positive_floats",
        "subtract_two_negative_floats",
        "subtract_zeros",
        "subtract_large_positive_numbers",
        "subtract_large_negative_numbers",
        "subtract_larger_from_smaller",
        "subtract_small_positive_floats",
        "subtract_small_negative_floats",
        "subtract_scientific_notation_large",
        "subtract_scientific_notation_small",
        "subtract_from_positive_infinity",
        "subtract_from_negative_infinity",
        "subtract_floating_point_precision",
        "subtract_positive_from_zero",
        "subtract_zero_from_positive",
    ]
)
def test_subtract(a: Number, b: Number, expected: Number) -> None:
    """
    Test the 'subtract' function with various combinations of integers and floats.

    This parameterized test verifies that the 'subtract' function correctly subtracts the
    second number from the first, handling both positive and negative values, as well as
    integers and floats. Parameterization allows for comprehensive testing of multiple cases.

    Parameters:
    - a (Number): The number from which to subtract.
    - b (Number): The number to subtract.
    - expected (Number): The expected result of the subtraction.

    Steps:
    1. Call the 'subtract' function with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    Example:
    >>> test_subtract(5, 3, 2)
    >>> test_subtract(-5, -3, -2)
    """
    # Call the 'subtract' function with the provided arguments
    result = subtract(a, b)
    
    # For floating point operations that might have precision issues, use pytest.approx
    if isinstance(a, float) or isinstance(b, float):
        assert result == pytest.approx(expected, rel=1e-9), f"Expected subtract({a}, {b}) to be {expected}, but got {result}"
    else:
        assert result == expected, f"Expected subtract({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Unit Tests for the 'multiply' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),           # Test multiplying two positive integers
        (-2, 3, -6),         # Test multiplying a negative integer with a positive integer
        (2.5, 4.0, 10.0),    # Test multiplying two positive floats
        (-2.5, 4.0, -10.0),  # Test multiplying a negative float with a positive float
        (0, 5, 0),            # Test multiplying zero with a positive integer
        (5, 0, 0),            # Test multiplying positive integer with zero
        (1, 100, 100),        # Test multiplying by 1 (identity)
        (-1, 100, -100),      # Test multiplying by -1 (negation)
        (1000, 1000, 1000000), # Test multiplying large numbers
        (-1000, -1000, 1000000), # Test multiplying two negative large numbers
        (0.5, 0.5, 0.25),     # Test multiplying small positive floats
        (-0.5, -0.5, 0.25),   # Test multiplying small negative floats
        (1e5, 1e5, 1e10),     # Test multiplying very large numbers in scientific notation
        (1e-5, 1e-5, 1e-10),  # Test multiplying very small numbers in scientific notation
        (float('inf'), 2, float('inf')),  # Test multiplying infinity
        (-float('inf'), 2, -float('inf')), # Test multiplying negative infinity
        (2.5, 4.8, 12.0),     # Test floating point precision
        (-7, 3, -21),         # Test negative times positive
        (7, -3, -21),         # Test positive times negative
        (-7, -3, 21),         # Test negative times negative
    ],
    ids=[
        "multiply_two_positive_integers",
        "multiply_negative_and_positive_integer",
        "multiply_two_positive_floats",
        "multiply_negative_float_and_positive_float",
        "multiply_zero_and_positive_integer",
        "multiply_positive_integer_and_zero",
        "multiply_by_one_identity",
        "multiply_by_negative_one",
        "multiply_large_positive_numbers",
        "multiply_large_negative_numbers",
        "multiply_small_positive_floats",
        "multiply_small_negative_floats",
        "multiply_scientific_notation_large",
        "multiply_scientific_notation_small",
        "multiply_positive_infinity",
        "multiply_negative_infinity",
        "multiply_floating_point_precision",
        "multiply_negative_times_positive",
        "multiply_positive_times_negative",
        "multiply_negative_times_negative",
    ]
)
def test_multiply(a: Number, b: Number, expected: Number) -> None:
    """
    Test the 'multiply' function with various combinations of integers and floats.

    This parameterized test verifies that the 'multiply' function correctly multiplies two numbers,
    handling both positive and negative values, as well as integers and floats. Parameterization
    enables efficient testing of multiple scenarios in a concise manner.

    Parameters:
    - a (Number): The first number to multiply.
    - b (Number): The second number to multiply.
    - expected (Number): The expected result of the multiplication.

    Steps:
    1. Call the 'multiply' function with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    Example:
    >>> test_multiply(2, 3, 6)
    >>> test_multiply(-2, 3, -6)
    """
    # Call the 'multiply' function with the provided arguments
    result = multiply(a, b)
    
    # For floating point operations that might have precision issues, use pytest.approx
    if isinstance(a, float) or isinstance(b, float):
        assert result == pytest.approx(expected, rel=1e-9), f"Expected multiply({a}, {b}) to be {expected}, but got {result}"
    else:
        assert result == expected, f"Expected multiply({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Unit Tests for the 'divide' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 3, 2.0),           # Test dividing two positive integers
        (-6, 3, -2.0),         # Test dividing a negative integer by a positive integer
        (6.0, 3.0, 2.0),       # Test dividing two positive floats
        (-6.0, 3.0, -2.0),     # Test dividing a negative float by a positive float
        (0, 5, 0.0),            # Test dividing zero by a positive integer
        (0, -5, 0.0),           # Test dividing zero by a negative integer
        (10, 1, 10.0),          # Test dividing by 1 (identity)
        (10, -1, -10.0),        # Test dividing by -1 (negation)
        (1000000, 1000, 1000.0), # Test dividing large numbers
        (-1000000, 1000, -1000.0), # Test dividing large negative by positive
        (1000000, -1000, -1000.0), # Test dividing large positive by negative
        (-1000000, -1000, 1000.0), # Test dividing large negative by negative
        (7.5, 2.5, 3.0),        # Test dividing positive floats
        (-7.5, 2.5, -3.0),      # Test dividing negative by positive float
        (7.5, -2.5, -3.0),      # Test dividing positive by negative float
        (-7.5, -2.5, 3.0),      # Test dividing negative by negative float
        (1e10, 1e5, 1e5),       # Test dividing large scientific notation
        (1e-10, 1e-5, 1e-5),    # Test dividing small scientific notation
        (22, 7, 22/7),          # Test division with repeating decimal
        (1, 3, 1/3),            # Test division resulting in repeating decimal
        (100, 0.1, 1000.0),     # Test dividing by small decimal
        (0.1, 100, 0.001),      # Test dividing small number by large
    ],
    ids=[
        "divide_two_positive_integers",
        "divide_negative_integer_by_positive_integer",
        "divide_two_positive_floats",
        "divide_negative_float_by_positive_float",
        "divide_zero_by_positive_integer",
        "divide_zero_by_negative_integer",
        "divide_by_one_identity",
        "divide_by_negative_one",
        "divide_large_positive_numbers",
        "divide_large_negative_by_positive",
        "divide_large_positive_by_negative",
        "divide_large_negative_by_negative",
        "divide_positive_floats",
        "divide_negative_by_positive_float",
        "divide_positive_by_negative_float",
        "divide_negative_by_negative_float",
        "divide_scientific_notation_large",
        "divide_scientific_notation_small",
        "divide_with_repeating_decimal",
        "divide_resulting_in_repeating_decimal",
        "divide_by_small_decimal",
        "divide_small_by_large",
    ]
)
def test_divide(a: Number, b: Number, expected: float) -> None:
    """
    Test the 'divide' function with various combinations of integers and floats.

    This parameterized test verifies that the 'divide' function correctly divides the first
    number by the second, handling both positive and negative values, as well as integers
    and floats. Parameterization allows for efficient and comprehensive testing across multiple cases.

    Parameters:
    - a (Number): The dividend.
    - b (Number): The divisor.
    - expected (float): The expected result of the division.

    Steps:
    1. Call the 'divide' function with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    Example:
    >>> test_divide(6, 3, 2.0)
    >>> test_divide(-6, 3, -2.0)
    """
    # Call the 'divide' function with the provided arguments
    result = divide(a, b)
    
    # Division always returns float, so use pytest.approx for precision issues
    assert result == pytest.approx(expected, rel=1e-9), f"Expected divide({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Negative Test Case: Division by Zero
# ---------------------------------------------

def test_divide_by_zero() -> None:
    """
    Test the 'divide' function with division by zero.

    This negative test case verifies that attempting to divide by zero raises a ValueError
    with the appropriate error message. It ensures that the application correctly handles
    invalid operations and provides meaningful feedback to the user.

    Steps:
    1. Attempt to call the 'divide' function with arguments 6 and 0, which should raise a ValueError.
    2. Use pytest's 'raises' context manager to catch the expected exception.
    3. Assert that the error message contains "Cannot divide by zero!".

    Example:
    >>> test_divide_by_zero()
    """
    # Use pytest's context manager to check for a ValueError when dividing by zero
    with pytest.raises(ValueError) as excinfo:
        # Attempt to divide 6 by 0, which should raise a ValueError
        divide(6, 0)
    
    # Assert that the exception message contains the expected error message
    assert "Cannot divide by zero!" in str(excinfo.value), \
        f"Expected error message 'Cannot divide by zero!', but got '{excinfo.value}'"

# ----------------------------------------------------
# Additional Edge Case Tests for Division by Zero
# ----------------------------------------------------

def test_divide_positive_by_zero() -> None:
    """Test dividing a positive number by zero raises ValueError."""
    with pytest.raises(ValueError) as excinfo:
        divide(10, 0)
    assert "Cannot divide by zero!" in str(excinfo.value)

def test_divide_negative_by_zero() -> None:
    """Test dividing a negative number by zero raises ValueError."""
    with pytest.raises(ValueError) as excinfo:
        divide(-10, 0)
    assert "Cannot divide by zero!" in str(excinfo.value)

def test_divide_float_by_zero() -> None:
    """Test dividing a float by zero raises ValueError."""
    with pytest.raises(ValueError) as excinfo:
        divide(5.5, 0.0)
    assert "Cannot divide by zero!" in str(excinfo.value)

def test_divide_zero_by_zero() -> None:
    """Test dividing zero by zero raises ValueError."""
    with pytest.raises(ValueError) as excinfo:
        divide(0, 0)
    assert "Cannot divide by zero!" in str(excinfo.value)

# ----------------------------------------------------
# Additional Test Cases for Floating Point Precision
# ----------------------------------------------------

def test_add_floating_point_precision_close() -> None:
    """Test addition with floating point numbers that are very close."""
    result = add(0.1 + 0.2, 0.0)
    expected = 0.3
    # Use pytest.approx for floating point comparison
    assert result == pytest.approx(expected, rel=1e-9)

def test_subtract_floating_point_precision_close() -> None:
    """Test subtraction with floating point precision issues."""
    result = subtract(0.3, 0.1)
    expected = 0.2
    # Use pytest.approx for floating point comparison
    assert result == pytest.approx(expected, rel=1e-9)

def test_multiply_floating_point_precision_close() -> None:
    """Test multiplication with floating point precision."""
    result = multiply(0.1, 0.3)
    expected = 0.03
    # Use pytest.approx for floating point comparison
    assert result == pytest.approx(expected, rel=1e-9)

def test_divide_floating_point_precision_close() -> None:
    """Test division with floating point precision."""
    result = divide(0.3, 0.1)
    expected = 3.0
    # Use pytest.approx for floating point comparison
    assert result == pytest.approx(expected, rel=1e-9)
