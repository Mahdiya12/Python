file = open('coding.txt' , 'r')

count = 0

readfile = file.read()

coList = readfile.split("\n")

for i in coList:

 if i:

   count += 1

print("the number of lines in the file: ")

print(count)