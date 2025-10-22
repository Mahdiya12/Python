class parrot: 

    #class atr=tribute
    species = "bird" 

    #intant attribute
    def __init__(self, name, age): 
       self.name = name
       self.age = age

    #creating instance

blu = parrot("blu", 10)
mac = parrot("mac", 5)

print("blu is a {}" .format(blu.species))
print("mac is also {}" .format(mac.species))

print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(mac.name, mac.age))




    