from src.is_palindrome import is_palindrome


def test_is_palindrome():
    assert is_palindrome("amanaplanacanalpanama") == True
    assert is_palindrome("racecar") == True
    assert is_palindrome("anutforajaroftuna") == True
    assert is_palindrome("WasitacaroracatIsaw") == True
