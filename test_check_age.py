import json
import pytest


def test_check_age():
    filename = "add_heroes.json"
    
    with open(filename, 'r') as f:
        data = json.load(f)

    older_30 = [hero['name'] for hero in data['members'] if hero['age'] > 30]
    assert older_30
