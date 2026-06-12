from funcoes import is_positive, lenght_of_string

def test_lenght_of_string():    
    assert lenght_of_string("Hello") == 5, "Expected length of 'Hello' to be 5"
    assert lenght_of_string("") == 0, "Expected length of empty string to be 0"
    assert lenght_of_string("Python") == 6, "Expected length of 'Python' to be 6"

def test_is_positive():
    assert is_positive(5) == True, "Expected 5 to be positive"
    assert is_positive(-3) == False, "Expected -3 to be not positive"
    assert is_positive(0) == False, "Expected 0 to be not positive"