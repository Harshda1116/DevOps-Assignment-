''' Read from a File
We used open in read mode and file.read to read and print to display.
'''

file = open("student.txt","r")

content = file.read()

print("File Content")
print(content)


file.close()

'''output

PS C:\Users\hp\Desktop\Harshda\DEVOPS ASSIGN\Python and Bash Assignment> python Assignment_que4.py
File Content
Name : Yash 
Course : Python 
File Handling program
PS C:\Users\hp\Desktop\Harshda\DEVOPS ASSIGN\Python and Bash Assignment> 
'''
