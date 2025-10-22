#Sum of First 10 Natural Numbers
num = 1
sum = 0
while(num<=10):
    sum = sum+num
    num = num+1
print("Sum of First 10 Natural Numbers :", sum)


#Multiplication Table of 17
num = 17
print("Table of 17")
for i in range(1,11):
    mul = num*i
    

    print("17 x %d = %d" % (i, mul))


#Prime Number Check for 29
num = 29
flag = False
if num > 1:

    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")