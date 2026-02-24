''' Read from a File
We used open in read mode and file.read to read and print to display.
'''

file = open("student.txt","r")

content = file.read()

print("File Content")
print(content)

file.close()