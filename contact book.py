contacts ={}
# add contacts
def add_contact(name,phone,email,address):
    contacts[name] = {'Phone':phone,'Email':email,'Address': address}

# view contact list
def view_contact_list():
    for name,details in contacts.items():
        print(f"{name}:{details['Phone']}")

# view search contact
def search_contact(query):
    results = [(name,details) for name, details in contacts.item() if query.lower() in name.lower() or query in details['Phone']] 
    return results
# update contact
def update_contact(name,phone, email, address):
    if name in contacts:
        contacts[name] = {'Phone': phone,'email': email,'Address': address }
        print(f"Contact{name} updated successfully.")
    else:
         print(f"Contact{name} not found.")

# delete contact
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted succeesfully.")
    else:
         print(f"Contact {name} not found.")
 
 # user interface
while True:

    print("\n Contact Book")
    print("1, Add Contact")
    print("2, View Contact list ")
    print("3, Search Contact")
    print("4, Update Contact")
    print("5,Delete Contact")
    print("Exit")

    choice = input(" Enter your choice(1-6):")

    if choice == '1':
        name = input("Enter your name:")
        phone  = input("Enter your phone number:")
        email= input("Enter your email:")
        address = input("Enter your address:")
        add_contact(name,phone, email,address)

    elif choice == '2':
        print("\nContact List:")
        view_contact_list()

    elif choice == '3' :
        query = input("Enter name or phone number to search:") 
        results= search_contact("query") 
        if results:
            print("\n Search Results:")
            for name, details in results:
                print(f"{name} :{ details['phone']}")
        else:
            print("No contact found.")

    elif choice == '4':
        name = input("Enter name of the contact to update:")
        phone = input("Enter new phone number:")
        email = input("Enter new email:")
        address = input("Enter new address:")
        update_contact(name,phone, email, address)

    elif choice == '5':
        name = input ("Enter name of the  contact to delete")
        delete_contact(name)

    elif choice == '6':
        print("Existing Program.")

    else:
        print("Invailed choice. Please enter a number between 1and 6" )







    




