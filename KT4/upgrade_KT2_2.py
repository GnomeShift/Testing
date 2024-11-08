import csv
import pytest

# функция для чтения данных из CSV-файла
def load_data_from_csv(file_path):
    with open(file_path, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        data = []
        for row in reader:
            # Преобразуем оценки и итоговую оценку в числа
            test_scores = [float(row['test1']), float(row['test2']), float(row['test3']), float(row['test4'])]
            final_grade = float(row['final_grade'])
            data.append((row['name'], test_scores, final_grade))
        return data

# функция для расчета итоговой среднего арифметического
def calculate_final_grade(test_scores):
    return sum(test_scores) / len(test_scores)
    
# тест 
@pytest.mark.parametrize("name, test_scores, expected_final_grade", load_data_from_csv("grades.csv"))
def test_student_final_grade(name, test_scores, expected_final_grade):
    calculated_final_grade = calculate_final_grade(test_scores)
    assert calculated_final_grade == expected_final_grade
