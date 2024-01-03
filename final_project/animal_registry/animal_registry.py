import json
from final_project.animals.pack_animals.pack_an import Camel, Horse, Donkey
from final_project.animals.pets.pets import Dog, Cat, Hamster


class AnimalRegistry:
    def __init__(self):
        self.animals = {}
        self.load_animals()

    def find_animal_by_identifier(self, identifier):
        for animal in self.animals.values():
            if str(animal.id) == identifier or animal.name.lower() == identifier.lower():
                return animal
        return None

    def load_animals(self):
        try:
            with open('animals.json', 'r') as file:
                data = json.load(file)
                self.animals = {}
                for id, item in data.items():
                    animal_type = item.get('type')
                    # Воссоздание экземпляров соответствующих классов
                    if animal_type == "Dog":
                        animal = Dog(item['name'])
                    elif animal_type == "Cat":
                        animal = Cat(item['name'])
                    elif animal_type == "Hamster":
                        animal = Hamster(item['name'])
                    elif animal_type == "Camel":
                        animal = Camel(item['name'])
                    elif animal_type == "Horse":
                        animal = Horse(item['name'])
                    elif animal_type == "Donkey":
                        animal = Donkey(item['name'])
                    else:
                        continue  # Неизвестный тип животного

                    animal._registered = item.get('registered', False)
                    animal._commands = item.get('commands', [])
                    self.animals[int(id)] = animal
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            print('Error decoding JSON file.')

    def save_animals(self):
        data = {
            str(animal.id): {
                'name': animal.name,
                'species': animal.species,
                'type': animal.__class__.__name__,
                'registered': animal._registered,
                'commands': animal._commands
            } for animal in self.animals.values()
        }
        with open('animals.json', 'w') as file:
            json.dump(data, file, indent=2)

    def add_animal(self, name, species):
        animal = None
        if species.lower() == "dog":
            animal = Dog(name)
        elif species.lower() == "cat":
            animal = Cat(name)
        elif species.lower() == "hamster":
            animal = Hamster(name)
        elif species.lower() == "camel":
            animal = Camel(name)
        elif species.lower() == "horse":
            animal = Horse(name)
        elif species.lower() == "donkey":
            animal = Donkey(name)

        if animal:
            self.animals[animal.id] = animal
            self.save_animals()
            print(f'{species} named "{name}" added with ID: {animal.id}')
        else:
            print("Unknown animal species.")

    def remove_animal(self, identifier):
        animal = self.find_animal_by_identifier(identifier)
        if animal:
            del self.animals[animal.id]
            self.save_animals()
            print(f'Animal with name/ID "{identifier}" removed.')
        else:
            print(f'Animal with name/ID "{identifier}" not found.')

    def view_animals(self):
        if not self.animals:
            print('No animals registered.')
            return

        print('Animal Registry:\n--------------------------------')
        for animal_id, animal in self.animals.items():
            status = 'Registered' if animal._registered else 'Not Registered'
            print(f'ID: {animal.id}\nName: {animal.name}\nSpecies: '
                  f'{animal.species}\nStatus - {status}\n'
                  f'Commands - {", ".join(animal._commands)}\n'
                  f'--------------------------------')

    def register_animal(self, identifier):
        animal = self.find_animal_by_identifier(identifier)
        if animal:
            animal._registered = True
            self.save_animals()
            print(f'Animal with name/ID "{identifier}" registered.')
        else:
            print(f'Animal with name/ID "{identifier}" not found.')