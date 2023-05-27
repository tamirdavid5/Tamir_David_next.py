class Animal:
    def __init__(self, name, hunger=0):
        self._name = name
        self._hunger = hunger
    def get_name(self):
        return self._name

    def is_hungry(self):
        return self._hunger > 0

    def feed(self):
        if self._hunger > 0:
            self._hunger -= 1
class Dog(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)

class Cat(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)

class Skunk(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)

class Unicorn(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)

class Dragon(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)