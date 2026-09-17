def sum_of_digits(n: int) -> int:
    """
    Calculates the sum of digits of a non-negative integer.

    Args:
        n (int): The number whose digits will be summed.

    Returns:
        int: Sum of the digits.

    Raises:
        TypeError: If input is not an integer.
        ValueError: If input is negative.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 0:
        raise ValueError("n must be a non-negative integer.")

    total = 0

    while n > 0:
        total = total + n % 10
        n = n // 10

    return total


if __name__ == "__main__":
    n = input("Enter your digit: ")

    try:
        n = int(n)
        result = sum_of_digits(n)
        print("Sum of digits:", result)

    except (TypeError, ValueError) as error:
        print("Error:", error)
