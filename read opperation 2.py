file = open('coding.txt' , 'r')
print("reading first line...")
print(file.readline())
file.close()

file = open('coding.txt' , 'r')
print("reading multiple lines...")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

