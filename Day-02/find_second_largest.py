def second_largest(nums: list[int]) -> int | None:
    """
    Find the second largest unique number in a list without sorting.

    Args:
        nums (list[int]): A list of integers.

    Returns:
        int | None: The second largest unique value, or None
        if there are fewer than two unique values.

    Raises:
        TypeError: If input is not a list or elements are not integers.
        ValueError: If the list has fewer than 2 elements.
    """
    # Validate that the input is a list.
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of integers.")

    # Validate that all elements are integers.
    if any(not isinstance(current_num, int) for current_num in nums):
        raise TypeError("All elements of the list should be integers.")

    # Check if the list has at least two elements.
    if len(nums) < 2:
        raise ValueError("List should contain at least two elements.")

    if nums[0] > nums[1]:
        largest = nums[0]
        second = nums[1]
    else:
        largest = nums[1]
        second = nums[0]

    for current_num in nums[2:]:
        if current_num > largest:
            second = largest
            largest = current_num

        elif current_num != largest and current_num > second:
            second = current_num

    # Check if a second unique value exists.
    if largest == second:
        return None

    return second


if __name__ == "__main__":
    nums = [1, 2, 22, 33333, 44444, 5555, 2000]

    try:
        result = second_largest(nums)
        print("Second largest:", result)

    except (TypeError, ValueError) as error:
        print(f"Error: {error}")
