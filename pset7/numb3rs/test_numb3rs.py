from numb3rs import validate

def test_valid_ips():
    # Testing valid IPv4 addresses
    assert validate("127.0.0.1") == True
    assert validate("192.168.1.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True

def test_invalid_ips():
    # Testing invalid IPv4 addresses
    assert validate("275.3.6.28") == False   # Number > 255
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False   # Number > 255
    assert validate("cat") == False          # Not a number
    assert validate("192.168.1") == False    # Incomplete address
    assert validate("192.168.1.abc") == False # Alphabet in address
