def calculate_factorial(n):
    """
    Calculates the factorial of a non-negative integer n.
    """
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0:
        return 1
    else:
        # Initialize result
        result = 1
        # Loop from 1 up to n (inclusive)
        for i in range(1, n + 1):
            result *= i
        return result

def check_even_odd(number):
    """
    Checks if a given number is even or odd.
    """
    if number % 2 == 0:
        print(f"{number} is an **Even** number.")
    else:
        print(f"{number} is an **Odd** number.")

# --- Execution ---

# 1. Factorial Calculation
print("## 🔢 Factorial Calculation")
num_factorial = 5
fact_result = calculate_factorial(num_factorial)
print(f"The factorial of **{num_factorial}** is: **{fact_result}**") # 5! = 120

# 2. Even/Odd Check
print("\n## ⚖️ Even/Odd Check")
number_to_check = 14
check_even_odd(number_to_check)

number_to_check = 27
check_even_odd(number_to_check)