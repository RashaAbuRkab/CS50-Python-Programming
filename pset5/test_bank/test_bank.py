from bank import value
def test_value():
    assert value("Hello") == 0
    assert value("Hey!") == 20
    assert value("Maha Ali <->") == 100
