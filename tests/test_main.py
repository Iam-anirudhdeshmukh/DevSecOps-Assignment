from src.test_app.main import greet

def test_greet():
    assert greet("Alice") == "Hello, Alice!"
    assert greet("") == "Hello, !"

# This test checks the greet function from the main module of the test application.
# It ensures that the function returns the expected greeting for given names.