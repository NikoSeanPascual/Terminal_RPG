student_grade = {}

while True:
    print("\n========== STUDENT GRADE ANALYZER ==========\n1. Add student,\n2. View students\n3. Class average\n4. Highest grade\n5. Lowest grade\n6. Exit")
    choice = input("Choose an option: ").lower().strip()
    if choice == "1":
        name = input("Student name: ")
        grade = float(input("Grade: "))
        student_grade[name] = grade
        print(f"{name} added!")
    elif choice == "2":
        if student_grade:
            print("=============== STUDENTS ===============")
            for name, grade in student_grade.items():
                print(f"{name}:{grade}")
        else:
            print("No students have been added yet, try adding some :)")
    elif choice == "3":
        if student_grade:
            avg = sum(student_grade.values())/len(student_grade)
            print(f"Class average: {avg:.2f}")
        else:
            print("No data to calculate average, are you sure you added some students")
    elif choice == "4":
        if student_grade:
            top_student = max(student_grade, key=student_grade.get)
            print(f"The best Student is {top_student} with {student_grade[top_student]} for he's grades, give them a compliment will ya.;)")
        else:
            print("No data to calculate Best Student, it seems you forgot to add students before calculating the average")
    elif choice == "5":
        if student_grade:
            low_student = min(student_grade, key=student_grade.get)
            print(f"The worst student is {low_student} with {student_grade[low_student]} for he's grades, you should probably talk to them about this. :(")
        else:
            print(f"No data to calculate the Worst student, are you sure you added some students")
    elif choice == "6":
        print("GOOD BYE!!")
        break