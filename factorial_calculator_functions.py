def get_non_negative_integer() -> int:
    """
    Obtains a non-negative integer input from the user.

    Returns:
        int: The validated non-negative integer.
    """
    while True:
        try:
            n = int(input("Enter a non-negative integer: "))
            if n >= 0:
                return n
            else:
                print("Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def calculate_factorial(n: int) -> int:
    """
    Calculates the factorial of a given non-negative integer.

    Args:
        n (int): The non-negative integer.

    Returns:
        int: The calculated factorial.
    """
    if n == 0:
        return 1
    else:
        factorial = 1
        for i in range(1, n + 1):  # Corrected loop range
            factorial *= i
        return factorial

# Main program flow
if __name__ == "__main__":
    number = get_non_negative_integer()
    factorial_result = calculate_factorial(number)
    print(f"The factorial of {number} is: {factorial_result}")