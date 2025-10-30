def no_notes(a):
    # List of denominations in descending order
    Q = [2000, 500, 200, 100, 50, 20, 10]
    
    # Iterate through the denominations
    for i in range(len(Q)):
        q = Q[i]  # q is the current denomination
        
        # Calculate the number of notes (x) for the current denomination (q)
        # Use integer division (//) to get the whole number of notes
        x = a // q
        
        # Print the result using the format shown in the screenshot
        print(f"Notes of {q} = {x}")
        
        # Update the remaining amount (a) using the modulo operator (%)
        # This is the amount left to be processed by smaller denominations
        a = a % q

# --- Main Execution ---
# Get the total amount from the user
# The screenshot shows an input of 9800
try:
    amount = int(input("Enter Total Amount"))
except ValueError:
    print("Invalid amount entered. Using default 9800.")
    amount = 9800

# Call the function with the entered amount
no_notes(amount)