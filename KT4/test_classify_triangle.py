from KT4.classify_triangle import classify_triangle
import pytest

@pytest.mark.parametrize("a, b, c, expected", [(2, 2, 2, "Равносторонний"), (5, 5, 6, "Равнобедренный"), (4, 5, 6, "Разносторонний"), (11, 5, 5, "Подозрительный какой-то...")])
def test_classify_triangle(a, b, c, expected):
    assert classify_triangle(a, b, c) == expected
