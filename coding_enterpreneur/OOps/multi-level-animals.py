# BASE CLASS
class Animal:
    noise = 'Rrrrr'
    color = 'white'

    def make_noise(self):
        print(self.noise)

    def change_noise(self, new_noise):
        self.noise = new_noise

    def make_color(self):
        print(self.color)

    def change_color(self, new_color):
        self.color = new_color

# CHILD CLASSES


class Wolf(Animal):
    noise = "Grrr"
    color = 'Brown'


class BabyWolf(Wolf):
    color = 'Brown and White'


wolf = BabyWolf()
wolf.make_noise()
wolf.make_color()
# animal = Animal()
# animal.make_noise()
# animal.change_noise('meow')
# animal.make_noise()
