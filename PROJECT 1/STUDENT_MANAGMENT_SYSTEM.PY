students = {}

while True:
    print("\n ===== SYSTEM MANAGMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Show Topper")
    print("7. Show Average Marks")
    print("8. Exit")

    choice = input("Enter a choice(1-8): ")

    # ADD A STUDENT 

    if choice == "1":
        Name = input("Enter a name: ").title() # .title() is used for converting the first letter of each word to uppercase and the rest to lowercase.

        if Name in students:
            print("Name already exists!")
        else:
            Marks = float(input("Enter a Marks: "))
            students[ Name ]= Marks
            print("Added Succesfully!")

    # VIEW STUDENT 
    elif choice == "2":
        if not  students:
            print("Record not found.")
        else:
            print("\n--- Student Record ---")
            for Name,Marks in students.items(): # .items() is used for returns both the key and value from the dictionary.
                print(f"{Name} : {Marks}")

    # SEARCH STUDENT 
    elif choice == "3":
            Name = input("Enter a name: ").title()

            if Name in students:
                print(f"{Name}'s Marks: {students[Name]}") # used here a f string.
            else:
                print("Record not found!")

    # UPDATE STUDENT 
    elif choice == "4":
        Name = input("Enter a name: ").title()

        if Name in students:
            New_Marks = float(input("Enter a new marks: "))
            students[Name] = New_Marks
            print("Marks updated succesfully")
        else:
            print("Marks not updated")

    # DELETE STUDENT 
    elif choice =="5":
        Name = input("Enter a name: ").title()

        if Name in students:
            del students[Name] # del is used for to remove a key-value pair from a dictionary.
            print("Deleted succesfully!")
        else:
            print("Not deleted")

    # SHOW TOPPERS 
    elif choice == "6":

        if not students:   
            print("Record not found")
        else:
            topper = max(students, key=students.get) # max() finds the largest value. and .get() is used for fetching the value associated with a key.
            print(f"Topper : {topper}")
            print(f"Marks : {students[topper]}")

    # AVERAGE MARKS 
    elif choice == "7":

        if not students:   
            print("Record not found")
        else:
            average = sum(students.values())/len(students) # sum() is used for adds all the numbers together. and len() returns the number of items.
            print(f"Average Marks: {average}")

    # EXIT 
    elif choice == "8":
        print("Exiting Management System")
        break
    else:
        print("Choose Number Between 1-8")