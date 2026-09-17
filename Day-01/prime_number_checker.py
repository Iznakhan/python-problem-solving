def find_prime(number: int) -> str:
    """
    Check whether a number is prime or not.

    Args:
        number (int): The number to check.

    Returns:
        str: A message stating whether the number is prime or not.

    Raises:
        TypeError: If number is not an integer.
        ValueError: If number is less than 2.
    """
    if not isinstance(number, int) or isinstance(number, bool):
        raise TypeError("number must be an integer.")

    if number < 2:
        raise ValueError("number must be greater than or equal to 2.")

    for i in range(2, number):
        if number % i == 0:
            return f"{number} is not a prime number."

    return f"{number} is a prime number."


if __name__ == "__main__":
    try:
        number = int(input("Enter a number: "))
        result = find_prime(number)
        print(result)

    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
