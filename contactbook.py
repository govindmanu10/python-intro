contact = {"anu": ["9067890123", "anu@gmail.com"]}
name = input("Enter the name of the contact: ")
phone = input("Enter the phone number of the contact: ")
gmail = input("Enter the gmail address of the contact: ")
contact[name] = [phone, gmail]
search_name = input(" Enter the name of the contact to search: ")
if search_name in contact:
    print("name:", search_name)
    print("phone:", contact[search_name][0])
    print("gmail:", contact[search_name][1])
else:
    print("Contact not found.")