from src.say_hello import say_hello


def test_say_hello():
    assert say_hello("James") == "Hello, James"
    assert say_hello("Jason") == "Hello, Jason"
    assert say_hello("Jeffrey") == "Hello, Jeffrey"
    assert say_hello("Jeremiah") == "Hello, Jeremiah"
    assert say_hello("Joseph") == "Hello, Joseph"
