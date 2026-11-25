from calculator import add, subtract, multiply, divide, CircleArea
from batch_calculator import process_calculation


def test_add():
	assert add(2, 3) == 5

def test_divide():
	assert divide(6, 2) == 3
	
def test_multiply():
    assert multiply(4, 2) == 8
    
def test_subtract():
    assert subtract(10, 4) == 6
    
def test_divide_uneven():
    # Arrange
    a, b = 5, 2
    # Act
    result = divide(a, b)
    # Assert
    assert result == 2.5

def test_CircleArea():
    assert CircleArea(-4) == "Error"
        
#def test_divide_by_zero_returns_error():
	#assert process_calculation("divide", "7", "0") == ("ERROR", "", "DIVISION_BY_ZERO")
