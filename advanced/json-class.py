import json


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User('akshit', 21)


def encode_user(obj):
    if isinstance(obj, User):
        return {
            "name": obj.name,
            "age": obj.age,
            obj.__class__.__name__: True
        }
    else:
        raise TypeError('Something went wrong!')


userJson = json.dumps(user, default=encode_user)
print(userJson)

user = json.loads(userJson)
print(user)
