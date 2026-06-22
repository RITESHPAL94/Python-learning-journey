contact = {}

while True:
    print("\n --- contact book ---")
    print("1. Add contact")
    print("2. View contact")
    print("3. update contact")
    print("4. delete contact")
    print("5. exit")

    choice = input("Enter a number(1-5): ")

    # ADD CONTACT 
    
    if "1" == choice:
        name = input("Enter a name: ")
        if name in contact:
            print("contact already exists!")
        else:
            phone_no = input("Enter a phone no.: ")
            contact[name] = phone_no
            print("Added succesfully!")

    # VIEW CONTACT 

    elif "2" == choice:
        if not contact:
            print("No contact yet!")
        else:
           ''' for name, phone_no in contact.items():
                print(f"{name} : {phone_no}")'''
           
           for name, phone_no in enumerate(contact.items(),1):
               print(f"{name} : {phone_no} ")

    # UPDATE CONTACT 
    elif "3" == choice:
        name = input("Enter a name: ")
        if name in contact:
            new_phone = input("Enter a new phone number: ")
            contact[name] = new_phone
            print("Contact updated succesfully!")
        else:
            print("Contact not found")

    # DELETE CONTACT 
    elif "4" == choice:
        name = input("Enter a name: ")
        if name not in contact:
            print("Contact not found")
        else:
            del contact[name] 
            print("Contact deleted succesfully!")

    # Exit 
    else:
        if "5" == choice:
            print("The program terminated")
            break
        else:
            print("Choose the number between 1 to 5")