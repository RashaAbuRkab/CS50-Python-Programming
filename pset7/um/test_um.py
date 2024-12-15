import um

def test_count_basic():
    assert um.count("um") == 1
    assert um.count("hello, um, world") == 1
    assert um.count("yummy") == 0

def test_count_case_insensitive():
    assert um.count("Um") == 1
    assert um.count("UM") == 1
    assert um.count("uM") == 1

def test_count_with_punctuation():
    assert um.count("um?") == 1
    assert um.count("Hello, um!") == 1
    assert um.count("Um, thanks for the album.") == 1
    assert um.count("Um, thanks, um...") == 2
    assert um.count("yum um!") == 1  # Should not count "yum"

def test_count_multiple_occurrences():
    assert um.count("Um um um!") == 3
    assert um.count("This is um, that is um.") == 2

def test_count_no_um():
    assert um.count("This text has no mention of that word.") == 0
