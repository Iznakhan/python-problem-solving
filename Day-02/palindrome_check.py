def find_palindrome(text: str) -> str:
    """
    Checks whether a string is a palindrome or not.

    Args:
        text (str): A string to be checked.

    Returns:
        str: Returns whether the string is a palindrome or not.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string.")

    rev_str = ""

    for char in text:
        rev_str = char + rev_str

    if rev_str == text:
        return "String is palindrome"
    else:
        return "String is not palindrome"


if __name__ == "__main__":
    try:
        text = input("Enter your text: ")
        result = find_palindrome(text)
        print(result)
    except TypeError as e:
        print(f"Error: {e}")
