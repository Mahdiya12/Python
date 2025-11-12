# Function 1: Note Denomination Calculation (Incomplete, based on image_83657d.png)
# Note: The array Q (denominations) is missing, so this function will cause an error
# without defining Q. For a runnable example, I will define a placeholder Q.
Q = [100, 50, 20, 10, 5, 1] # Placeholder denominations
def no_notes(a):
    for i in range(len(Q)): # Iterating through denominations Q
        q = Q[i]
        x = a // q # Integer division to find number of notes
        print("Notes of {} = {}".format(q, x))
        a = a % q # Remainder for next calculation

# Function 2: Fibonacci Series (from image_836827.png)
def fib_series(nterms):
    # first two terms
    n1, n2 = 0, 1
    count = 0
    while count < nterms:
        print(n1)
        nth = n1 + n2
        # update values
        n1 = n2
        n2 = nth
        count += 1

# --- Execution of the combined simple code ---

# 1. Basic and Inverted Star Patterns (from image_836575.png)
print("--- Basic Star Pattern ---")
print("Star Pattern \n")
for i in range(1,6):
    for j in range(i):
        print("*", end="")
    print('\n')

print("--- Inverted Star Pattern ---")
print("Inverted Star Pattern \n")
for i in range(6,1,-1):
    for j in range(i, 1, -1):
        print("*", end="")
    print('\n')

# 2. Fibonacci Series Execution (Simplified input for a small example)
print("\n--- Fibonacci Series Example ---")
terms = 5 # Using a fixed small number instead of input()
if terms <= 0:
    print("Please enter a positive integer")
elif terms == 1:
    print("Fibonacci sequence upto", terms, ":")
    fib_series(terms)
else:
    print("Fibonacci sequence:")
    fib_series(terms)

# 3. Note Denomination Calculation (Simplified input for a small example)
print("\n--- Note Denomination Example ---")
amount = 178 # Using a fixed small number instead of input()
print(f"Calculating notes for amount: {amount}")
no_notes(amount)