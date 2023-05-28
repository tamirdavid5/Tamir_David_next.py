#Name: Tamir David

class Animal:

    zoo_name = "Hayaton"  # Shared attribute for all animals

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

    def talk(self):
        pass
class Dog(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)

    def talk(self):
        print("Woof woof")

    def fetch_stick(self):
        print("There you go, sir!")

class Cat(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)

    def talk(self):
        print("Meow")

    def chase_laser(self):
        print("Meeeeow")

class Skunk(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)
        self._stink_count = 6

    def talk(self):
        print("Tsssss")

    def stink(self):
        print("Dear lord!")

class Unicorn(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)

    def talk(self):
        print("Good day, darling")

    def sing(self):
        print("I’m not your toy...")

class Dragon(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)
        self._color = "Green"
    def talk(self):
        print("Raaaawr")

    def breath_fire(self):
        print("$@#$#@$")

def main():
    # Create animals and save instances in zoo_lst
    zoo_lst = []
    zoo_lst.append(Dog("Brownie", hunger=10))
    zoo_lst.append(Cat("Zelda", hunger=3))
    zoo_lst.append(Skunk("Stinky", hunger=0))
    zoo_lst.append(Unicorn("Keith", hunger=7))
    zoo_lst.append(Dragon("Lizzy", hunger=1450))

    # Create new animals and add them to zoo_lst
    zoo_lst.append(Dog("Doggo", hunger=80))
    zoo_lst.append(Cat("Kitty", hunger=80))
    zoo_lst.append(Skunk("Stinky Jr.", hunger=80))
    zoo_lst.append(Unicorn("Clair", hunger=80))
    zoo_lst.append(Dragon("McFly", hunger=80))

    # Iterate over animals in zoo_lst
    for animal in zoo_lst:
        if animal.is_hungry():
            print(f"{animal.__class__.__name__} {animal.get_name()}")
            while animal.is_hungry():
                animal.feed()
        animal.talk()

        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
            print(f"Stink count: {animal._stink_count}")
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()
            print(f"Color: {animal._color}")

    print("Zoo Name:", Animal.zoo_name)


if __name__ == "__main__":
    main()

