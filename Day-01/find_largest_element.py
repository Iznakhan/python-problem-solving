def find_largest(list1: list) -> int | float | None:
    """
    Find the largest element in a list.

    Args:
        list1 (list): A list containing integers and floats.

    Returns:
        int | float | None: The largest number, or None if
        the list contains duplicate values.

    Raises:
        TypeError: If input is not a list.
        ValueError: If the list is empty or contains non-numeric elements.
    """
    # Check if input is a list.
    if not isinstance(list1, list):
        raise TypeError("list1 must be a list.")

    # Check if the list is empty.
    if list1 == []:
        raise ValueError("List should not be empty.")

    # Check if all elements are numeric.
    for element in list1:
        if not isinstance(element, (int, float)):
            raise ValueError("List must contain only numbers.")

    # Duplicate values are not allowed.
    if len(list1) != len(set(list1)):
        return None

    largest = list1[0]

    for num in list1:
        if num > largest:
            largest = num

    return largest


if __name__ == "__main__":
    list1 = input("Enter numbers by commas: ")
    list1 = [float(x) for x in list1.split(",")]

    result = find_largest(list1)
    print(result)
