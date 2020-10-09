class Computer:
    def __init__(self, cpu, ram) -> None:
        self.cpu = cpu
        self.ram = ram                  # it's used when you need to use it in methods / fuctions
        # print("-----It's work as a contructor.-----")

    def config(self):
        print("CPU :", self.cpu)
        print("RAM :", self.ram, "GB")                 # like this


computer1 = Computer('i5', 8)
computer2 = Computer('Ryzan 5', 16)
# Computer('i3', 4) - object creation, just constructor called
# Computer.config(computer1)
computer1.config()
computer2.config()
