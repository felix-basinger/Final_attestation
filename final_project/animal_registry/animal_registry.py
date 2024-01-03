import json
from final_project.animals.pack_animals.pack_an import Camel, Horse, Donkey
from final_project.animals.pets.pets import Dog, Cat, Hamster


# Класс, в котором описывается логика работы приложения
# и обозначены все функции, задействованые в работе
class AnimalRegistry:
    def __init__(self):
        self.animals = {}
        self.load_animals()

    def find_animal_by_identifier(self, identifier):
        for animal in self.animals.values():
            if str(animal.id) == identifier or animal.name.lower() == identifier.lower():
                return animal
        return None

# Функция создания JSON файла, хранящего информацию о животных
# Информация хранится в файле в виде вложенных списков
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

# Функция записи информации в JSON файл и сохранение этой информации
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

# Функция добавления животного в реестр питомника
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

# Функция удаления животного из реестра
    def remove_animal(self, identifier):
        animal = self.find_animal_by_identifier(identifier)
        if animal:
            del self.animals[animal.id]
            self.save_animals()
            print(f'Animal with name/ID "{identifier}" removed.')
        else:
            print(f'Animal with name/ID "{identifier}" not found.')

# Функция просмотра животных, содержащихся в реестре
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

# Функция регистрации животного в реестре
    def register_animal(self, identifier):
        animal = self.find_animal_by_identifier(identifier)
        if animal:
            animal._registered = True
            self.save_animals()
            print(f'Animal with name/ID "{identifier}" registered.')
        else:
            print(f'Animal with name/ID "{identifier}" not found.')

# Функция обучения животного командам
# Команды хранятся в списке конкретного животного в виде списка
    def teach_command(self, identifier, command):
        found = False
        for animal in self.animals.values():
            if str(animal.id) == identifier or animal.name.lower() == identifier.lower():
                animal.add_command(command)
                self.save_animals()
                print(f'Command "{command}" added to animal with name/ID "{identifier}".')
                found = True
                break
        if not found:
            print(f'Animal with name/ID "{identifier}" not found.')

# Функция поиска животного по имени или его ID
    def search_by_id(self, identifier):
        animal = self.find_animal_by_identifier(identifier)
        if animal:
            status = 'Registered' if animal._registered else 'Not Registered'
            print(f'Animal with name/ID "{identifier}":\n--------------------------------\nName: {animal.name}\n'
                  f'Species: {animal.species}\n'
                  f'Status - {status}\n'
                  f'Commands - {", ".join(animal._commands)}\n'
                  f'--------------------------------')
        else:
            print(f'Animal with name/ID "{identifier}" not found.')

# Функция поиска животных по какому-либо ключевомуу слову из их описания
    def search_by_keyword(self, keyword):
        result_animals = []
        keyword = keyword.lower()

        for animal_id, animal in self.animals.items():
            if keyword in str(animal.id).lower() or keyword in animal.name.lower() or keyword in animal.species.lower():
                result_animals.append(animal)

        if not result_animals:
            print(f'No animals containing "{keyword}" found.')
        else:
            print(f'Animals containing "{keyword}":\n--------------------------------')
            for animal in result_animals:
                status = 'Registered' if animal._registered else 'Not Registered'
                print(f'ID: {animal.id}\nName: {animal.name}\nSpecies: '
                      f'{animal.species}\n'
                      f'Status - {status}\nCommands - {", ".join(animal._commands)}\n'
                      f'--------------------------------')

# Функция показа класса, к котрому относится животное
# (класс животного определяется в фунции add_animal)
    def display_animal_type(self, identifier):
        animal = self.find_animal_by_identifier(identifier)
        if animal:
            if isinstance(animal, Dog):
                animal_type = "Dog"
            elif isinstance(animal, Cat):
                animal_type = "Cat"
            elif isinstance(animal, Hamster):
                animal_type = "Hamster"
            elif isinstance(animal, Camel):
                animal_type = "Camel"
            elif isinstance(animal, Horse):
                animal_type = "Horse"
            elif isinstance(animal, Donkey):
                animal_type = "Donkey"
            else:
                animal_type = "Unknown"

            print(f'Animal with name/ID "{identifier}" is a {animal_type}.')
        else:
            print(f'Animal with name/ID "{identifier}" not found.')
