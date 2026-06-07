student = {}

while True:
    print("\n-----STUDENT MANAGER APP------")
    print("1. Add student ")
    print("2. View Students ")
    print("3. Check Result ")
    print("4. Exit ")

    choice = input("enter your choice: ")

    #Add students
    if choice == "1":
        name = input("enter student name: ")
        marks = int(input("Enter marks: "))
        student[name] = marks
        #rahul 50
        print(f"{name} Successfully Added!")

    #view students
    elif choice == "2":
        if not student:
            print("No student found!")
        else:
            for name, marks in student.items():
                print(name, ":", marks)

    #check result
    elif choice == "3":
        name = input("Enter student name: ")

        if name in student:
            marks = student[name]
      
            if marks >= 40:
                print("PASS")
            else:
                print("FAIL")
        
        else:
            print("Student not found!")

    #exit
    elif choice == "4":
        print("Exiting.......")
        break

    else:
        print("In-valid input")