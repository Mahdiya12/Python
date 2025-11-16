file = open('coding mp.txt' , 'r')

print(file.read())

file.close()

file = open('coding mp.txt' , 'w')

file.write("hello! this is Mahdiya and i'm an athlete!")

file.close()

file = open('coding mp.txt' , 'a')

file.write("for sure i love playing different sports! although i do enjoy maths and science!")

file.close()
