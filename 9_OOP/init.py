class Student:
    schoolName = "ABC School"

    def __init__(self, name, course):
        # print("Whenever a new object is created I am called automically")
        self.name = name
        self.course = course


student1 = Student("Shivangi", "B.Tech")  # init methond will be called
print("Student1 Name-", student1.name)
print("Student1 Course-", student1.course)

student2 = Student("Akhilesh", "BCA")
print("Student2 Course-", student2.name)
print("Student2 Course-", student2.course)
