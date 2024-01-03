class Animal:
    animal_count = 0

    def __init__(self, name, species, registered=False, commands=None):
        Animal.animal_count += 1
        self._id = Animal.animal_count
        self._name = name
        self._species = species
        self._registered = registered
        self._commands = commands if commands else []

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def species(self):
        return self._species

    def add_command(self, command):
        self._commands.append(command)

    def get_commands(self):
        return ', '.join(self._commands)
