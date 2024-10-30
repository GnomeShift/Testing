from KT3.string_length import string_length

def test_multiline():
    assert string_length("многострочная\nстрока") == 21
