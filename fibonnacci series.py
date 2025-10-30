def fib_series(nterms):
    # first two terms
    n1, n2 = 0, 1
    count = 0

    # Check if the number of terms is valid inside the function for consistency, 
    # although the main program logic handles the initial checks.
    if nterms <= 0:
        print("Please enter a positive integer")
        return
    elif nterms == 1:
        print("Fibonacci sequence upto 1:")
        print(n1)
        return

    # Loop to generate the sequence
    while count < nterms:
        print(n1)
        nth = n1 + n2  # Calculate the next term
        
        # update values
        n1 = n2        # Update n1 to the previous n2
        n2 = nth       # Update n2 to the newly calculated term (nth)
        count += 1     # Increment the counter


# --- Main Execution Logic ---

# Get the number of terms from the user (matching the console prompt)
try:
    nterms = int(input("How many terms? "))
except ValueError:
    nterms = 0 # Set to 0 to trigger the error message or default behavior

if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print(f"Fibonacci sequence upto {nterms}:")
    fib_series(nterms)
else:
    # This print statement matches the output shown in the screenshot for nterms > 1
    print("Fibonacci sequence:")
    fib_series(nterms)