def prime_numbers(start: int, end: int) -> None:
    """
    Prints all prime numbers between the given start and end values.

    Args:
        start (int): Starting number of the range.
        end (int): Ending number of the range.

    Raises:
        TypeError: If start or end is not an integer.
        ValueError: If start is greater than end.
    """
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("start and end must be integers.")

    if start > end:
        raise ValueError("start must be less than or equal to end.")

    for numbers in range(start, end + 1):
        for i in range(2, numbers):
            if numbers % i == 0:
                break
        else:
            print(numbers)


if __name__ == "__main__":
    prime_numbers(100, 200)
