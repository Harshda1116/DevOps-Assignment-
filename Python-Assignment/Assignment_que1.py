'''1. Grade Checker
Take a score as input and print the grade based on the following:
90+ : "A"
80-89 : "B"
70-79 : "C"
60-69 : "D"
Below 60 : "F"
here we used a basic if else statement to carry out marks and all.
'''
score = int(input("Enter your marks:\n"))

if score >= 90:
    grade = "A"

elif score >=80:
    grade = "B"

elif score >=70:
    grade = "C"

elif score >=60:
    grade = "D"

else:
    grade = "F"

print("Your grade is ",grade)


'''Output
PS C:\Users\hp\Desktop\Harshda\DEVOPS ASSIGN\Python and Bash Assignment> python Assignment_que1.py
Enter your marks:
90
Your grade is  A
PS C:\Users\hp\Desktop\Harshda\DEVOPS ASSIGN\Python and Bash Assignment> python Assignment_que1.py
Enter your marks:
60
Your grade is  D
PS C:\Users\hp\Desktop\Harshda\DEVOPS ASSIGN\Python and Bash Assignment'''
