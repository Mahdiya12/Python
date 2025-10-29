# empty dictionary

my_dict = {}

#dictionaries with integers only

my_dict = {1:"Apple" , 2: "Ball" }

#dictionary with mixed keys

my_dict = {"name" : "Mahdiya" , 1 : [1,2,4,5]}

my_dict = {"name":"Mahdiya" , "age" : "12"}

print(my_dict["name"])
print(my_dict.get("age"))

my_dict['age'] = 13

print(my_dict)

my_dict['gender'] = 'female'

print(my_dict)

my_dict.pop('age')
print(my_dict)

my_dict.clear


