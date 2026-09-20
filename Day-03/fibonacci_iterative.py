def fibonacci_seq(n:int)->None:
    """
    This function prints Fibonacci sequence.

    Args:
        n (int): A number to compute.

    Returns:
        None

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is less than or equal to zero.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n <= 0:
        raise ValueError("n must be greater than zero.")

    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


if __name__ == "__main__":
    try:
        n = int(input("Enter a number: "))
        fibonacci_seq(n)

    except (TypeError, ValueError) as error:
        print("Error:", error)
