from plates import is_valid


def test_length():
    assert is_valid("AB") == True  # Minimum length
    assert is_valid("ABCDEFG") == False  # More than 6 characters

def test_start_with_letters():
    assert is_valid("AB123") == True  # Starts with two letters
    assert is_valid("1ABC") == False  # Starts with a number

def test_only_alphanumeric():
    assert is_valid("ABC123") == True  # Only alphanumeric
    assert is_valid("ABC!@#") == False  # Contains special characters

def test_numbers_at_end():
    assert is_valid("ABC123") == True  # Numbers at the end
    assert is_valid("ABC12A") == False  # Number followed by a letter
    assert is_valid("ABC012") == False  # Numbers starting with '0'

def test_edge_cases():
    assert is_valid("A1") == False  # Too short, one letter and one number
    assert is_valid("AB") == True  # Valid two-character plate
    assert is_valid("A") == False  # Only one character

