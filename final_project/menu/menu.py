from final_project.animal_registry.animal_registry import AnimalRegistry


def main_menu():
    animal_registry = AnimalRegistry()
    while True:
        print(
            '\n1. Add Animal\n2. Remove Animal\n3. View Animals\n4. Register Animal\n'
            '5. Teach Command\n6. Search by name or ID\n7. Search by Keyword\n8. Display Animal Type\n9. Exit')
        choice = input('Enter your choice (1-9): ')

        if choice == '1':
            name = input('Enter animal name: ')
            species = input('Enter animal species: ')
            animal_registry.add_animal(name, species)
        else:
            print('Invalid choice. Please enter a number between 1 and 9.')