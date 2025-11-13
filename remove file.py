file1 = open('coding.txt' , 'r')
file2 = open('codingal update.txt' , 'w')

for line in file1.readline():

   if not (line.startswith("it")):
       
       print(line)

       file2.write(line)

file1.close()
file2.close()