
def classify_triangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Подозрительный какой-то..."
    
    if a == b == c:
        return "Равносторонний"
    elif a == b or a == c or b == c:
        return "Равнобедренный"
    else:
        return "Разносторонний"

print(classify_triangle(2, 4, 7))
