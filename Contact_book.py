import json


def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)

        return contacts

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []            


contacts = load_contacts()

def show_menu():
    print("1 - Add contact")
    print("2 - Show contacts")
    print("3 - Search by city")
    print("4 - Search by name")
    print("5 - Delete contact")
    print("6 - Edit contact")
    print("0 - Exit")

def get_name(prompt):
    name = input(prompt).strip().capitalize()

    if not name:
        print("Name cannot be empty")
        return None

    return name


def get_phone(prompt):
    phone = input(prompt).strip()

    if not phone:
        print("Phone cannot be empty")
        return None

    return phone


def get_city(prompt):
    city = input(prompt).strip().capitalize()

    if not city:
        print("City cannot be empty")
        return None

    return city

def get_optional_name(prompt, current_name):
    
    name = input(prompt).strip().capitalize()

    if not name:
        return current_name
    
    return name

def get_optional_phone(prompt, current_phone):

    phone = input(prompt).strip()

    if not phone:
        return current_phone
    
    return phone

def get_optional_city(prompt, current_city):

    city = input(prompt).strip().capitalize()

    if not city:
        return current_city
    
    return city


def add_contact(contacts):

    name = get_name("Enter name: ")

    if name is None:
        return

    phone = get_phone("Enter phone: ")

    if phone is None:
        return
    
    city = get_city("Enter city: ")

    if city is None:
        return

    contact = {
        "name": name,
        "phone": phone,
        "city": city
    }

    contacts.append(contact)
    save_contacts(contacts)

    print("Contact added")

def print_contact(index, contact):
    print(f'{index}. {contact["name"]} | {contact["phone"]} | {contact["city"]}')

def search_contacts(contacts, key, value):
    
    found = False

    for index, contact in enumerate(contacts, start=1):

        if contact[key] == value:
            print_contact(index, contact)
            found = True
    
    return found


def search_by_city(contacts):
    city = input("Enter city: ").strip().capitalize()

    if not city:
        print("City cannot be empty")
        return

    found = search_contacts(contacts, "city", city)

    if not found:
        print("No contacts in this city")


def search_by_name(contacts):
    name = input("Enter name: ").strip().capitalize()

    if not name:
        print("Name cannot be empty")
        return
    
    found = search_contacts(contacts, "name", name)

    if not found:
        print("No contacts with this name")

def edit_contact(contacts):
    if not contacts:
        print("No contacts to edit")
        return

    show_contacts(contacts)

    try:
        number = int(input("Enter contact number: "))
    
    except ValueError:
        print("Contact number must be a number")
        return

    if number < 1 or number > len(contacts):
        print("Invalid contact number")
        return

    index = number - 1
    contact = contacts[index]

    print("Current contact:")
    print(number, contact)

    new_name = get_optional_name("Enter new name or press enter to keep current: ", contact["name"])

    new_phone = get_optional_phone("Enter new phone or press enter to keep current: ", contact["phone"])

    new_city = get_optional_city("Enter new city or press enter to keep current: ", contact["city"])

    contact["name"] = new_name
    contact["phone"] = new_phone
    contact["city"] = new_city

    save_contacts(contacts)

    print("Contact updated")                  

                

def show_contacts(contacts):

    if not contacts:
        print("No contacts yet")
        return

    for index, contact in enumerate(contacts, start=1):
        print_contact(index, contact)

def delete_contact(contacts):
    if not contacts:
        print("No contacts to delete")
        return

    show_contacts(contacts)

    try:
        number = int(input("Enter contact number: "))
    except ValueError:
        print("Contact number must be a number")
        return

    if number < 1 or number > len(contacts):
        print("Invalid contact number")
        return

    index = number - 1
    deleted_contact = contacts.pop(index)
    save_contacts(contacts)

    print("Deleted:", deleted_contact["name"])            


def run_app():
    while True:
        show_menu()

        choice = input("Choose option: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            show_contacts(contacts)
        elif choice == "3":
            search_by_city(contacts)
        elif choice == "4":
            search_by_name(contacts)    
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            edit_contact(contacts)                
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Wrong choice")

        print()

if __name__ == "__main__":
    run_app()