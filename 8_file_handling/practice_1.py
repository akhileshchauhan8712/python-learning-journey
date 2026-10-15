# Write code to open a file named demo.txt in read mode.

file = open("python_with_saumya_singh/8_file_handling/demo.txt", "r")
data = file.read()
print("My name is Akhilesh\n", data)

# Write a program to read a text from a given file certificate.txt and find whether it contains the word live.
file = open("python_with_saumya_singh/8_file_handling/certificate.txt", "r")
dataOfFile = file.read()

dataOfFile = dataOfFile.lower()
if "live" in dataOfFile:
    print("Yes Live word is present in the file")
else:
    print("No")

# Open a file called report.txt in write mode.
file = open("python_with_saumya_singh/8_file_handling/report.txt", "w")
file.write(
    "Python is a high-level, interpreted, general-purpose programming language known for its simple and readable syntax."
)

with open("python_with_saumya_singh/8_file_handling/report.txt", "r") as f:
    data = f.read()
    print("File Data", data)
print(len(data))
