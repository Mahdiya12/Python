# Class for Computer Science Students
class CSStudent:
    # Class attribute
    stream = "CSE"

    # Instance attribute
    def __init__(self, roll, name):
        self.roll = roll
        self.name = name

    # Instance method to set address
    def setAddress(self, address):
        self.address = address

    # Instance method to get address
    def getAddress(self):
        return self.address

    # Method to show student info
    def displayInfo(self):
        return f"Name: {self.name}, Roll: {self.roll}, Stream: {self.stream}, Address: {self.address}"


# Class for Parrots
class Parrot:
    # Class attribute
    species = "Bird"

    # Instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance methods
    def sing(self, song):
        return f"{self.name} is singing '{song}'"

    def dance(self):
        return f"{self.name} is dancing!"


# Creating CSStudent objects
student1 = CSStudent(101, "Mahdiya")
student1.setAddress("Dhaka")
print(student1.displayInfo())

# Creating Parrot objects
blu = Parrot("Blu", 10)
mac = Parrot("Mac", 5)

print(f"{blu.name} is a {blu.species}")
print(f"{mac.name} is also a {mac.species}")

print(f"{blu.name} is {blu.age} years old")
print(f"{mac.name} is {mac.age} years old")

print(blu.sing("Rewrite the Stars"))
print(mac.dance())
