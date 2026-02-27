'''3.Write to a File
Write a program to create a text file and write some content to it.

Using file functions like write and open.
'''

file = open("student.txt", "w")

file.write("Name : Yash \n")
file.write("Course : Python \n")
file.write("File Handling program")

file.close()

print("Successful")

''' output
PS C:\Users\hp\Desktop\Harshda\DEVOPS ASSIGN\Python and Bash Assignment> python Assignment_que3.py
Successful
PS C:\Users\hp\Desktop\Harshda\DEVOPS ASSIGN\Python and Bash Assignment>  '''
