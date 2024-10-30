import json


def add_hero(filename):
    # грузим старых
    with open("superhero.json", 'r') as f:
        old = json.load(f)

    # копируем в новый файл
    with open("superhero_new.json", 'w') as f:
        json.dump(old, f, indent=4)
        
    # грузим новых
    with open(filename, 'r') as f:
        new = json.load(f)

    new_heroes = [member['name'] for member in new['members']]
    new_members = [{"name": name, "age": 30} for name in new_heroes]

    # грузим добавленных
    with open("superhero_new.json", 'r') as f:
        existing = json.load(f)
    
    existing['members'].extend(new_members)
    
    # сохраняем
    with open("superhero_new.json", 'w') as f:
        json.dump(existing, f, indent=4)


def sort_hero(filename):
    with open(filename, 'r') as f:
        data = json.load(f)

    data['members'].sort(key=lambda member: member['age'])

    with open('superhero_new.json', 'w') as f:
        json.dump(data, f, indent=4)


def check_age(filename):
    with open(filename, 'r') as f:
        data = json.load(f)

    older_30 = [hero['name'] for hero in data['members'] if hero['age'] > 30]
    return older_30


add_hero("add_heroes.json")
sort_hero("superhero_new.json")
check_age("superhero_new.json")
