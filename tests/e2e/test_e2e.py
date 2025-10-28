# tests/e2e/test_e2e.py

import pytest  # Import the pytest framework for writing and running tests

# The following decorators and functions define E2E tests for the FastAPI calculator application.

@pytest.mark.e2e
def test_hello_world(page, fastapi_server):
    """
    Test that the homepage displays "Hello World".

    This test verifies that when a user navigates to the homepage of the application,
    the main header (`<h1>`) correctly displays the text "Hello World". This ensures
    that the server is running and serving the correct template.
    """
    # Navigate the browser to the homepage URL of the FastAPI application.
    page.goto('http://localhost:8000')
    
    # Use an assertion to check that the text within the first <h1> tag is exactly "Hello World".
    # If the text does not match, the test will fail.
    assert page.inner_text('h1') == 'Hello World'

@pytest.mark.e2e
def test_calculator_add(page, fastapi_server):
    """
    Test the addition functionality of the calculator.

    This test simulates a user performing an addition operation using the calculator
    on the frontend. It fills in two numbers, clicks the "Add" button, and verifies
    that the result displayed is correct.
    """
    # Navigate the browser to the homepage URL of the FastAPI application.
    page.goto('http://localhost:8000')
    
    # Fill in the first number input field (with id 'a') with the value '10'.
    page.fill('#a', '10')
    
    # Fill in the second number input field (with id 'b') with the value '5'.
    page.fill('#b', '5')
    
    # Click the button that has the exact text "Add". This triggers the addition operation.
    page.click('button:text("Add")')
    
    # Use an assertion to check that the text within the result div (with id 'result') is exactly "Result: 15".
    # This verifies that the addition operation was performed correctly and the result is displayed as expected.
    assert page.inner_text('#result') == 'Calculation Result: 15'

@pytest.mark.e2e
def test_calculator_divide_by_zero(page, fastapi_server):
    """
    Test the divide by zero functionality of the calculator.

    This test simulates a user attempting to divide a number by zero using the calculator.
    It fills in the numbers, clicks the "Divide" button, and verifies that the appropriate
    error message is displayed. This ensures that the application correctly handles invalid
    operations and provides meaningful feedback to the user.
    """
    # Navigate the browser to the homepage URL of the FastAPI application.
    page.goto('http://localhost:8000')
    
    # Fill in the first number input field (with id 'a') with the value '10'.
    page.fill('#a', '10')
    
    # Fill in the second number input field (with id 'b') with the value '0', attempting to divide by zero.
    page.fill('#b', '0')
    
    # Click the button that has the exact text "Divide". This triggers the division operation.
    page.click('button:text("Divide")')
    
    # Use an assertion to check that the text within the result div (with id 'result') is exactly
    # "Error: Cannot divide by zero!". This verifies that the application handles division by zero
    # gracefully and displays the correct error message to the user.
    assert page.inner_text('#result') == 'Error: Cannot divide by zero!'

@pytest.mark.e2e
def test_calculator_subtract(page, fastapi_server):
    """
    Test the subtraction functionality of the calculator.

    This test simulates a user performing a subtraction operation using the calculator
    on the frontend. It fills in two numbers, clicks the "Subtract" button, and verifies
    that the result displayed is correct.
    """
    # Navigate the browser to the homepage URL of the FastAPI application.
    page.goto('http://localhost:8000')
    
    # Fill in the first number input field (with id 'a') with the value '10'.
    page.fill('#a', '10')
    
    # Fill in the second number input field (with id 'b') with the value '3'.
    page.fill('#b', '3')
    
    # Click the button that has the exact text "Subtract". This triggers the subtraction operation.
    page.click('button:text("Subtract")')
    
    # Use an assertion to check that the text within the result div (with id 'result') shows the correct result.
    assert page.inner_text('#result') == 'Calculation Result: 7'

@pytest.mark.e2e
def test_calculator_multiply(page, fastapi_server):
    """
    Test the multiplication functionality of the calculator.

    This test simulates a user performing a multiplication operation using the calculator
    on the frontend. It fills in two numbers, clicks the "Multiply" button, and verifies
    that the result displayed is correct.
    """
    # Navigate the browser to the homepage URL of the FastAPI application.
    page.goto('http://localhost:8000')
    
    # Fill in the first number input field (with id 'a') with the value '6'.
    page.fill('#a', '6')
    
    # Fill in the second number input field (with id 'b') with the value '7'.
    page.fill('#b', '7')
    
    # Click the button that has the exact text "Multiply". This triggers the multiplication operation.
    page.click('button:text("Multiply")')
    
    # Use an assertion to check that the text within the result div (with id 'result') shows the correct result.
    assert page.inner_text('#result') == 'Calculation Result: 42'

@pytest.mark.e2e
def test_calculator_divide(page, fastapi_server):
    """
    Test the division functionality of the calculator.

    This test simulates a user performing a division operation using the calculator
    on the frontend. It fills in two numbers, clicks the "Divide" button, and verifies
    that the result displayed is correct.
    """
    # Navigate the browser to the homepage URL of the FastAPI application.
    page.goto('http://localhost:8000')
    
    # Fill in the first number input field (with id 'a') with the value '20'.
    page.fill('#a', '20')
    
    # Fill in the second number input field (with id 'b') with the value '4'.
    page.fill('#b', '4')
    
    # Click the button that has the exact text "Divide". This triggers the division operation.
    page.click('button:text("Divide")')
    
    # Use an assertion to check that the text within the result div (with id 'result') shows the correct result.
    assert page.inner_text('#result') == 'Calculation Result: 5'

@pytest.mark.e2e
def test_calculator_sequential_operations(page, fastapi_server):
    """
    Test performing multiple sequential operations without page refresh.

    This test simulates a user performing multiple calculations in sequence,
    verifying that the calculator can handle multiple operations correctly.
    """
    # Navigate the browser to the homepage URL of the FastAPI application.
    page.goto('http://localhost:8000')
    
    # First operation: 5 + 3 = 8
    page.fill('#a', '5')
    page.fill('#b', '3')
    page.click('button:text("Add")')
    assert page.inner_text('#result') == 'Calculation Result: 8'
    
    # Second operation: 10 - 4 = 6 (reusing the same input fields)
    page.fill('#a', '10')
    page.fill('#b', '4')
    page.click('button:text("Subtract")')
    assert page.inner_text('#result') == 'Calculation Result: 6'
    
    # Third operation: 3 * 9 = 27
    page.fill('#a', '3')
    page.fill('#b', '9')
    page.click('button:text("Multiply")')
    assert page.inner_text('#result') == 'Calculation Result: 27'

@pytest.mark.e2e
def test_calculator_decimal_numbers(page, fastapi_server):
    """
    Test the calculator with decimal numbers.

    This test verifies that the calculator correctly handles floating-point numbers
    by performing an operation with decimal inputs.
    """
    # Navigate the browser to the homepage URL of the FastAPI application.
    page.goto('http://localhost:8000')
    
    # Fill in decimal numbers
    page.fill('#a', '2.5')
    page.fill('#b', '1.5')
    
    # Perform addition with decimal numbers
    page.click('button:text("Add")')
    
    # Verify the result shows correct decimal calculation
    assert page.inner_text('#result') == 'Calculation Result: 4'

@pytest.mark.e2e
def test_calculator_negative_numbers(page, fastapi_server):
    """
    Test the calculator with negative numbers.

    This test verifies that the calculator correctly handles negative numbers
    by performing operations with negative inputs.
    """
    # Navigate the browser to the homepage URL of the FastAPI application.
    page.goto('http://localhost:8000')
    
    # Fill in negative numbers
    page.fill('#a', '-10')
    page.fill('#b', '5')
    
    # Perform addition with negative number
    page.click('button:text("Add")')
    
    # Verify the result shows correct calculation with negative numbers
    assert page.inner_text('#result') == 'Calculation Result: -5'
