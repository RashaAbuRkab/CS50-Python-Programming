from twttr import shorten

def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("Rasha") == "Rsh"
    assert shorten("Maha") == "Mh"
    assert shorten("1234") == "1234"  # Ensure numbers are retained
    assert shorten("Hello, World!") == "Hll, Wrld!"  # Ensure punctuation is retained
    assert shorten("AEIOU") == ""  # Ensure uppercase vowels are removed
