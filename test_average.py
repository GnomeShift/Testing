import pytest
from average import average_grade

path = "grades.csv"

def test_average_grade():
    average = average_grade("grades.csv")
    assert average == 10
