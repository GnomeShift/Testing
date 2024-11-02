from KT4.is_even import is_even
import pytest

@pytest.mark.parametrize("number, expected", [(2, True), (3, False), (4, True)])
def test_is_even(number, expected):
    assert is_even(number) == expected
