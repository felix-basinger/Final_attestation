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
        elif choice == '2':
            identifier = input('Enter animal name or ID to remove: ')
            animal_registry.remove_animal(identifier)
        elif choice == '3':
            animal_registry.view_animals()
        elif choice == '4':
            identifier = input('Enter animal name or ID to register: ')
            animal_registry.register_animal(identifier)
        elif choice == '5':
            identifier = input('Enter animal name or ID: ')
            command = input('Enter command to teach: ')
            animal_registry.teach_command(identifier, command)
        elif choice == '6':
            identifier = input('Enter animal name or ID to search: ')
            animal_registry.search_by_id(identifier)
        elif choice == '9':
            print('Exiting the program.')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 9.')