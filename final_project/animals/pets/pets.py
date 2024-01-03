from final_project.animals.animals import Animal


class Pet(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)


class Dog(Pet):
    def __init__(self, name):
        super().__init__(name, "Dog")


class Cat(Pet):
    def __init__(self, name):
        super().__init__(name, "Cat")


class Hamster(Pet):
    def __init__(self, name):
        super().__init__(name, "Hamster")
