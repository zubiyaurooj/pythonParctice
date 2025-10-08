students = {}

while True:
    print("\n=== Student Report System ===")
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Find Topper")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        print(f"{name} added successfully!")

    elif choice == "2":
        if not students:
            print("No records found.")
        else:
            print("\n--- Student List ---")
            for name, marks in students.items():
                print(f"{name}: {marks}")

    elif choice == "3":
        if not students:
            print("No students available.")
        else:
            topper = max(students, key=students.get)
            print(f"Topper: {topper} with {students[topper]} marks")

    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")
