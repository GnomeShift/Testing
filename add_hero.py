import json

def add_hero(filename):
    # Грузим старых героев
    with open("superhero.json", 'r') as f:
        old = json.load(f)

    # Грузим новых героев
    with open(filename, 'r') as f:
        new = json.load(f)

    # Добавляем новых героев в список
    old['members'].extend(new['members'])

    # Сохраняем обновленный список героев
    with open("superhero_new.json", 'w') as f:
        json.dump(old, f, indent=4)

add_hero("add_heroes.json")
