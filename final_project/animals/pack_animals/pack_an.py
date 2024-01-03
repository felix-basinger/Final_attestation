from final_project.animals.animals import Animal


class Pack(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)


class Camel(Pack):
    def __init__(self, name):
        super().__init__(name, "Camel")


class Horse(Pack):
    def __init__(self, name):
        super().__init__(name, "Horse")


class Donkey(Pack):
    def __init__(self, name):
        super().__init__(name, "Donkey")
