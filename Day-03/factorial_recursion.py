def factorial(n : int)->int:
    """
    Calculates factorial of a number by using recursive function.

    Args:
        n (int): A non-negative integer to compute.

    Returns:
        int: Returns a non-negative integer.

    Raises:
        ValueError: If n is a negative integer.
        TypeError: If n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 0:
        raise ValueError("n must be equal to or greater than zero.")

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


if __name__ == "__main__":
    try:
        n = int(input("Enter a Number: "))
        result = factorial(n)
        print(result)

    except (TypeError, ValueError) as error:
        print("Error:",error)
