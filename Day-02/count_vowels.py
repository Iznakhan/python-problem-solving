def count_vowels(word: str) -> int:
    """
    Counts the number of vowels in a string.

    Args:
        word (str): The string to check for vowels.

    Returns:
        int: Returns the number of vowels.

    Raises:
        TypeError: If word is not a string.
    """
    if not isinstance(word, str):
        raise TypeError("word must be a string.")

    vowels = "aeiou"
    count = 0

    for char in word.lower():
        if char in vowels:
            count += 1

    return count


if __name__ == "__main__":
    try:
        word = input("Enter your word: ")
        result = count_vowels(word)
        print(result)
    except TypeError as e:
        print(f"Error: {e}")
