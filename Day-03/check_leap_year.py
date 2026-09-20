def check_leap(year: int) -> bool:
    """
    Checks whether a year is a leap year or not.

    Args:
        year (int): A year to be checked.

    Returns:
        bool: Returns True if the year is a leap year,
        otherwise False.

    Raises:
        TypeError: If year is not an integer.
        ValueError: If year is less than or equal to zero.
    """
    if not isinstance(year, int):
        raise TypeError("year must be an integer.")

    if year <= 0:
        raise ValueError("year must be greater than zero.")

    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False


if __name__ == "__main__":
    try:
        year = int(input("Enter a year: "))
        result = check_leap(year)
        print(result)

    except (TypeError, ValueError) as error:
        print("Error:", error)
