import json


def sort_hero(filename):
    with open(filename, 'r') as f:
        data = json.load(f)

    data['members'].sort(key=lambda member: member['age'])

    with open('superhero_new.json', 'w') as f:
        json.dump(data, f, indent=4)


sort_hero("superhero_new.json")
