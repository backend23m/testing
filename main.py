import json
from datetime import datetime

file_name = 'data.json'

def read_file(file_name: str) -> str:
    f = open(file=file_name)
    data = f.read()
    f.close()
    return data

def to_dict(data: str) -> dict:
    try:
        numbers = json.loads(data)
    except json.decoder.JSONDecodeError:
        numbers = {
            "numbers": []
        }

    return numbers

def sum_of_numbers(numbers: dict) -> int:
    s = 0
    for number in numbers['numbers']:
        s += number

    return s

def oldest_person(persons: list) -> dict:
    return min(persons, key=lambda person: datetime.strptime(person['birthday'], "%Y-%m-%d"))

data = read_file(file_name)
persons = to_dict(data)
person = oldest_person(persons)

print(person)