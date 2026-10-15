# Function Definiton with Parameters
def average(a=10, b=20):
    averageValue = int((a + b) / 2)
    print(averageValue)


# Function Calling with Arguments
average(5, 5)
average(25, 25)
average(50, 50)
average(30, 50)
average()


# Write a function show_age(name, age) that prints: "Saumya Singh is 21 years old."
def show_age(name="Akhilesh", age=26):
    print(f"{name} is {age} years old.")


show_age("Akhilesh", 20)
show_age()
show_age("Ramjanam", 26)
