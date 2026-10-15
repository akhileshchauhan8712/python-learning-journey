# Dictionary basics
student = {"name": "Akhilesh", "city": "Azamgarh", "age": "26", "rollNumber": 1}

print(type(student))
print(student["name"])
print(student)
print(student["city"])

student["city"] = "Bengaluru"
print(student)

student["favSubject"] = "English"
print(student)

student.pop("favSubject")
print(student)
print(student.items())
