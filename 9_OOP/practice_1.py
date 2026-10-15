# Create a class Car with attribute brand = "Scorpio".


class Car:
    brand = "Scorpio"


obj1 = Car()
print("Brand name is - ", obj1.brand)


# Create a class Laptop with attributes: brand, RAM, price.
#  Create 2 objects with different values
class Laptop:
    brand = "Dell"
    RAM = "8GB"
    price = "60000"


laptop1 = Laptop()
laptop1.brand = "Lenovo"
laptop1.RAM = "16GB"
print("Laptop1 Brand - ", laptop1.brand)

laptop2 = Laptop()
laptop2.brand = "HP"
print("Laptop2 Brand - ", laptop2.brand)
