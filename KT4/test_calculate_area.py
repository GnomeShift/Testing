from KT4.calculate_area import calculate_area
import pytest

@pytest.mark.parametrize("length, width, expected", [(2, 4, 8), (5, 3, 15), (15, 10, 150)])
def test_calculate_area(length, width, expected):
    assert calculate_area(length, width) == expected
