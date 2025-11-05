# --- Dictionary Operations ---
# Create a dictionary with mixed keys, as seen in the examples
my_dict = {'name': 'Jack', 'age': 26, 1: [2, 4, 3]}

# Access a value using the key (like the 'name' example)
print(f"Initial Name: {my_dict['name']}")

# Update a value (like the 'age' example)
my_dict['age'] = 27
print(f"Updated Dictionary: {my_dict}")

# Remove a particular element (like the 'pop' example)
my_dict.pop('age')
print(f"After pop('age'): {my_dict}")

# --- Tuple Operations ---
# Create a tuple with mixed datatypes, as seen in the examples
my_tuple = (1, "Hello", 3.4, 't')
print(f"The Tuple: {my_tuple}")

# Access a tuple element using indexing (like the my_tuple[0] example)
print(f"Element at index 0: {my_tuple[0]}")

# Slicing the tuple (like the my_tuple[1:4] example)
print(f"Sliced Tuple (0:3): {my_tuple[0:3]}")

# Iterating through the tuple (like the 'for letter in my_tuple' example)
print("Iterating:")
for item in my_tuple:
    print(f"-> {item}")