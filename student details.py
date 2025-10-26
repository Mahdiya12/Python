class CSStudent:


    stream = 'cse'


    def __init__(self, roll):

        self.roll = roll

    def setAddress(self, address):
        self.address = address


    def getAddress(self):
        return self.address


a = CSStudent(101)
b = CSStudent(102)

print(a.stream)  
print(b.stream) 
print(a.roll)    

print(CSStudent.stream)  