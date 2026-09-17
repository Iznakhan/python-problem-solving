def find_factorial(num: int) -> int:
    """
    Finds the factorial of a number.

    Args:
        num (int): A non-negative integer to compute.

    Returns:
        int: The factorial of the given number.

    Raises:
        TypeError: If num is not an integer.
        ValueError: If num is a negative integer.
    """
    if not isinstance(num, int):
        raise TypeError("num must be an integer.")

    if num < 0:
        raise ValueError("num must be a non-negative integer.")

    if num == 0:
        return 1

    for i in range(num - 1, 0, -1):
        num *= i

    return num


if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        result = find_factorial(num)
        print(result)
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
