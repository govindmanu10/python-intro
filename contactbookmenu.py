contacts = {}
while True:
    choice = input("1. add contact 2. Search contact 3. Exit Enter your choice: ")
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        if name not in contacts:
            contacts[name] = (phone, email)
            contact[name].append((phone, email))
        else:
            print("Contact already exists.")
    elif choice == "2":
        search = input("Enter name to search: ")
        if search in contacts:
            phone, email = contacts[search]
            print(f"Name: {search} Phone: {phone}Email: {email}")
        else:
            print(search, "not found.")
    elif choice == "3":
        break
    else:
        print("Invalid choice.")