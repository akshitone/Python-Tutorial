import simplejson as json
import os

if os.path.isfile("./Py3-Udemy/ages.json") and os.stat("./Py3-Udemy/ages.json"):

    old_file = open("./Py3-Udemy/ages.json", "r+")
    data = json.loads(old_file.read())
    print("Current age is", data["age"], "---adding a year.")
    data["age"] += 1
    print("New age is", data["age"])

else:

    old_file = open("./Py3-Udemy/ages.json", "w+")
    data = {"name": "Akshit", "age": 22}
    print("No file found, setting default age to", data["age"])

old_file.seek(0)
old_file.write(json.dumps(data))
