import pytest


# Function to test
def add_numbers(a, b):
    return a + b


# Fixture: reusable test data
@pytest.fixture
def sample_numbers():
    return 10, 20


# Test 1: Normal values
def test_add_numbers():
    assert add_numbers(2, 3) == 5


# Test 2: Zero boundary case
def test_add_numbers_with_zero():
    assert add_numbers(5, 0) == 5


# Test 3: Negative values
def test_add_numbers_negative_values():
    assert add_numbers(-2, -3) == -5


# Test 4: Fixture test
def test_add_numbers_with_fixture(sample_numbers):
    a, b = sample_numbers
    assert add_numbers(a, b) == 30


# Test 5: Large numbers
def test_add_numbers_large_values():
    assert add_numbers(1000000, 2000000) == 3000000


# Test 6: Parametrized tests
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (10, 20, 30),
        (-5, 5, 0),
        (0, 0, 0),
        (-3, -7, -10),
    ],
)
def test_add_numbers_parametrized(a, b, expected):
    assert add_numbers(a, b) == expected