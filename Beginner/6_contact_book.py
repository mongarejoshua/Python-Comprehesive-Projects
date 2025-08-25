import json

contacts = {}

def main():
    print("--- CONTACTS' MAIN MENU ---")
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
            save_contact()
            break
        else:
            print('Invalid choice')
            continue

def add():
    name = input('Enter contact name: ')
    phone = input('Enter your mobile number: ')
    email = input('Enter your email: ')
    
    contacts[name] = {'Phone': phone, 'Email': email}
    print(f"Contact '{name}' added successfully.\n")

def save_contact():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)
    print("Contacts saved successfully.")

def load_contacts():
    global contacts
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
        print("Contacts loaded successfully.")
    except FileNotFoundError:
        print("Contact book is currently empty.")

def view():
    if not contacts:
        print("No contacts\n")
    for name, det in contacts.items():
        print(f"Name: {name}\n Phone: {det['Phone']}\n Email: {det['Email']}\n" )

def remove():
    pass

def search():
    pass


if __name__ == "__main__":
    load_contacts()
    main()