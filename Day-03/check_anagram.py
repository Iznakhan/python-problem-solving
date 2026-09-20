def check_anagram(str1: str, str2: str) -> bool:
    """
    Checks whether strings are anagrams of each other or not.

    Args:
        str1 (str): A string to be checked.
        str2 (str): A string to be checked.

    Returns:
        bool: Returns True if strings are anagrams, otherwise False.

    Raises:
        TypeError: If str1 or str2 is not a string.
    """

    # Check that both inputs are strings
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError("Both str1 and str2 must be strings.")

    # Dictionary to store the count of each character
    char_count = {}

    # Start by assuming the strings are anagrams
    is_anagram = True

    # Different lengths means they cannot be anagrams
    if len(str1) != len(str2):
        is_anagram = False

    else:
        # Count each character in the first string
        for char in str1.lower():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        # Check the second string using the character counts
        for char in str2.lower():

            # Character is not present in the first string
            if char not in char_count:
                is_anagram = False
                break

            # Use one count for this character
            char_count[char] -= 1

            # If count becomes negative, second string has
            # more of this character than the first string
            if char_count[char] < 0:
                is_anagram = False
                break

    return is_anagram


if __name__ == "__main__":
    try:
        str1 = input("Enter a word: ")
        str2 = input("Enter a word: ")

        result = check_anagram(str1, str2)
        print(result)

    except TypeError as error:
        print("Error:", error)
