import json
person = {
    "name": "akshit",
    "age": 21,
    "city": "surat",
    "has_children": False,
    "title": ["Python developer", "NodeJS developer"]
}

personJSON = json.dumps(person, indent=4, sort_keys=True)
# print(personJSON)

# with open('person.json', 'w') as file:
#     json.dump(person, file, indent=4)

# person = json.loads(personJSON)
# print("FROM DATA: ", person)

with open('person.json', 'r') as file:
    person = json.load(file)

print("FROM FILE: ", person)
