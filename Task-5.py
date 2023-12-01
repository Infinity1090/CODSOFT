# Contact Book in Python.

contacts = []
def add_contact(name, phone, email, address):
    contact = {"name": name, "phone": phone, "email": email, "address": address}
    contacts.append(contact)
    print("Contact added successfully!")
def list_contacts():
    if not contacts:
        print("No contacts to display.")
    else:
        print("Contacts:")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact['name']} - {contact['phone']}")
def search_contact(query):
    results = []
    for contact in contacts:
        if query in contact['name'] or query in contact['phone']:
            results.append(contact)
    if results:
        print("Search results:")
        for contact in results:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")
    else:
        print("No contacts found.")
def update_contact(name, phone, new_name, new_phone, new_email, new_address):
    for contact in contacts:
        if contact['name'] == name and contact['phone'] == phone:
            contact['name'] = new_name
            contact['phone'] = new_phone
            contact['email'] = new_email
            contact['address'] = new_address
            print("Contact updated successfully!")
            return
    print("Contact not found.")
def delete_contact(name, phone):
    for contact in contacts:
        if contact['name'] == name and contact['phone'] == phone:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")
while True:
    print("\nContact Book")
    print("1. Add Contact")
    print("2. List Contacts")
    print("3. Search Contacts")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        add_contact(name, phone, email, address)
    elif choice == "2":
        list_contacts()
    elif choice == "3":
        query = input("Enter name or phone number to search: ")
        search_contact(query)
    elif choice == "4":
        name = input("Enter current name: ")
        phone = input("Enter current phone: ")
        new_name = input("Enter new name: ")
        new_phone = input("Enter new phone: ")
        new_email = input("Enter new email: ")
        new_address = input("Enter new address: ")
        update_contact(name, phone, new_name, new_phone, new_email, new_address)
    elif choice == "5":
        name = input("Enter name to delete: ")
        phone = input("Enter phone to delete: ")
        delete_contact(name, phone)
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
