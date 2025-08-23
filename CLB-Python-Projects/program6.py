# contact book program 
import json

contacts = {}

def main():
    print('--- CONTACTS MENU ---')
    while True:
        print('1. View contact list')
        print('2. Add a contact')
        print('3. Remove a contact')
        print('4. Search for a contact')
        print('5. Exit')

        user_choice = input('Enter an option number(i.e 1,2,3): ')

        if user_choice == '1':
            view()
        elif user_choice == '2':
            add()
        elif user_choice == '3':
            remove()
        elif user_choice == '4':
            search()
        elif user_choice == '5':
            break
        else:
            print('Invalid choice')
            continue

def view():
    pass

def add():
    pass

def remove():
    pass

def search():
    pass
