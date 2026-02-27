'''Student Grades
Create a dictionary where the keys are student names and the values are their grades. Allow the user to:
Add a new student and grade.
Update an existing student’s grade.
Print all student grades.

Used dictionary and basic operations. Using if else:
'''
student_grade = {}

while True:

    print("\n Student Grade Management")
    print("1. Add New Student")
    print("2. Update Student Grade")
    print("3. Print All Student Grades")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter Student name: ")
        grade = input("Enter grade: ")

        if name in student_grade:
            print("Student already exists!")
        else:
            student_grade[name] = grade
            print("Student added successfully.")
    
    elif choice == '2':
        name = input("Enter student name to update: ")
        
        if name in student_grade:
            grade = input("Enter new grade: ")
            student_grade[name] = grade
            print("Grade updated successfully.")
        else:
            print("Student not found.")

    elif choice == '3':
        if student_grade:
            print("\nStudent Grades:")
            for name, grade in student_grade.items():
                print(name, ":", grade)
        else:
            print("No student records available.")

    elif choice == '4':
        print("Exiting program.")
        break

    else:

        print("Invalid choice. Please try again.")

'''output

PS C:\Users\hp\Desktop\Harshda\DEVOPS ASSIGN\Python and Bash Assignment> python Assignment_que2.py

 Student Grade Management
1. Add New Student
2. Update Student Grade    
3. Print All Student Grades
4. Exit
Enter your choice: 1
Enter Student name: Harshda
Enter grade: A
Student added successfully.

 Student Grade Management  
1. Add New Student
2. Update Student Grade    
3. Print All Student Grades
4. Exit
Enter your choice: 3

Student Grades:
Harshda : A

 Student Grade Management
1. Add New Student
2. Update Student Grade
3. Print All Student Grades
4. Exit
Enter your choice: 2
Enter student name to update: Harshda
Enter new grade: B
Grade updated successfully.

 Student Grade Management
1. Add New Student
2. Update Student Grade
3. Print All Student Grades
4. Exit
Enter your choice: 3

Student Grades:
Harshda : B

 Student Grade Management
1. Add New Student
2. Update Student Grade
3. Print All Student Grades
4. Exit
Enter your choice: 4
Exiting program.'''
