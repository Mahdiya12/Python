# Empty tuple
my_tuple = ()
print(f"Empty tuple: {my_tuple}")

# Tuple having integers
my_tuple = (1, 2, 3)
print(f"Integer tuple: {my_tuple}")

# Tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(f"Mixed tuple: {my_tuple}")

# Nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(f"Nested tuple: {my_tuple}")

# Accessing tuple elements using indexing
# CORRECTED: Changed index 5 (out of bounds) to a valid index, 2.
print(f"Element at index 2: {my_tuple[2]}") 

# Nested tuple for indexing examples
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# Nested index
# n_tuple[0][3] -> The character at index 3 of the string 'mouse' which is 's'
print(f"Nested index [0][3] (string): {n_tuple[0][3]}")
# n_tuple[1][1] -> The element at index 1 of the list [8, 4, 6] which is 4
print(f"Nested index [1][1] (list): {n_tuple[1][1]}")

# Slicing
print(f"Sliced my_tuple[1:4]: {my_tuple[1:4]}")

# Iterating through tuple
print("\nIterating through tuple:")
for item in (my_tuple):
    print("Hello", item)