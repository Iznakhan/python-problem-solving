from typing import Any


def remove_duplicates(list1: list[Any]) -> list[Any]:
    """
    Remove duplicates from a list while maintaining original order.

    Args:
        list1 (list[Any]): A list containing any type of elements.

    Returns:
        list[Any]: A new list with duplicates removed.

    Raises:
        TypeError: If input is not a list.
        ValueError: If the list is empty.
    """
    if not isinstance(list1, list):
        raise TypeError("Input must be a list.")

    if len(list1) == 0:
        raise ValueError("list1 must not be empty.")

    result = []

    for i in list1:
        if i not in result:
            result.append(i)

    return result


if __name__ == "__main__":
    numbers_list = [200, 19, 20, 200, 3, 2, 2, 2, 44, 44, 19]

    try:
        result = remove_duplicates(numbers_list)
        print("After removing duplicates:", result)

    except (TypeError, ValueError) as error:
        print("Error:", error)
