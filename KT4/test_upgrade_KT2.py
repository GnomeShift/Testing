import pytest
import pandas as pd

@pytest.mark.parametrize("test1, test2, test3, test4, final, expected", [(10, 20, 30, 40, 50, 30), (21, 35, 42, 13, 8, 20), (24,68, 39, 81, 97, 60)])
def test_upgrade_average_grade(test1, test2, test3, test4, final, expected):
    df = pd.DataFrame({'Test1': [test1], 'Test2': [test2], 'Test3': [test3], 'Test4': [test4], 'Final': [final]})
    grades = df[['Test1', 'Test2', 'Test3', 'Test4', 'Final']]
    average = grades.mean()
    assert average.mean() == expected
