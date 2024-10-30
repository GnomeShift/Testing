
string = "строка"
filename = "string.txt"

def string_to_file(string, filename):
    with open(filename, "w", encoding="UTF-8") as f:
        f.write(string)
        f.close()
    
    print("Готово!")

string_to_file(string, filename)
