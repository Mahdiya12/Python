file = open('coding.txt' , 'r')

print(file.read())

file.close()

file = open('coding.txt' , 'r')

print("opening the first 15 characters")

print(file.read(15))

file.close()