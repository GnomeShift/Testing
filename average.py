import pytest
import pandas as pd

def average_grade(path):
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip().str.replace('"', '')
    grades = df[['Test1', 'Test2', 'Test3', 'Test4', 'Final']].values.flatten()
    average = grades.mean()
    print(f"Среднее: {average}")
    return average
