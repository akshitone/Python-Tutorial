x = "1"
print(type(x.upper()))


class Anything():
    def __init__(self, name):
        print("I want to print everytime...")
        self.name = name

    def any_str(self, str):
        return str.upper(), self.name.lower()


anything = Anything("AkshitOne")
# something = Anything("Complusory")
name, username = anything.any_str("Akshit Mithaiwala")
print(name, "-", username)
