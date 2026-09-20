def count_characters(text : str)-> dict:
    """
    Counts characters of a string.

    Args:
        text (str): A string to be counted.

    Returns:
        dict: Returns a dictionary of character occurrences.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string.")

    char_count = {}

    for char in text.lower().replace(" ", ""):
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


if __name__ == "__main__":
    try:
        text = input("Enter your text: ")
        result = count_characters(text)
        print(result)

    except TypeError as error:
        print("Error:", error)
