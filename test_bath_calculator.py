from batch_calculator import process_calculation

def test_Add_two_numbers():
	assert process_calculation("add", "10", "3") == ("OK", 13, "")

def test_Subtract_two_numbers():
	assert process_calculation("subtract", "25", "5") == ("OK", 20, "")
	
def test_Multiply_two_numbers():
	assert process_calculation("multiply", "3", "6") == ("OK", 18, "")

def test_divide_two_numbers():
	assert process_calculation("divide", "60", "5") == ("OK", 12, "")
        
def test_Divide_by_zero_returns_error():
	assert process_calculation("divide", "7", "0") == ("ERROR", "", "DIVISION_BY_ZERO")
	
def test_Unknown_operation():
	assert process_calculation("Percentage", "20", "4") == ("ERROR", "", "UNKNOWN_OPERATION")
	
def test_Whitespaces():
	assert process_calculation(" divide ", " 20 ", " 2 ") == ("OK", 10, "")
	
def test_calculaticon_with_decimals():
	assert process_calculation("divide", "12.5", "2.5") == ("OK", 5, "")

def test_Negative_number():
	assert process_calculation("add", "-7", "4") == ("OK", -3, "")
	
def test_Invalid_number():
	assert process_calculation("add", "hi", "9") == ("ERROR", "", "INVALID_NUMBER")

def test_Empty_operand():
	assert process_calculation("add", "", "2") == ("ERROR", "", "INVALID_NUMBER")

def test_Unknown_operation_has_priority():
    assert process_calculation("Percentage", "hi", "4") == ("ERROR", "", "UNKNOWN_OPERATION")

def test_Invalid_number_has_priority_over_division_by_zero():
    assert process_calculation("divide", "hi", "0") == ("ERROR", "", "INVALID_NUMBER")
