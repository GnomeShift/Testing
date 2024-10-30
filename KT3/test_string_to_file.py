from KT3.string_to_file import string_to_file

def test_string_to_file():
    string = "строка"
    filename = "test_string.txt"
    string_to_file(string, filename)
    
    with open(filename, "r", encoding="UTF-8") as f:
        assert f.read() == string
