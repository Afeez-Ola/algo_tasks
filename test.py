def map_array_to_string_index(arr, string):
    """Maps elements in an array to their corresponding indices in a string.

    Args:
        arr: A list of numbers.
        string: A string.

    Returns:
        A dictionary mapping each number to its index in the string.
    """

    string = string.lower()
    result = {}

    for num in arr:
        hex_str = format(num, 'x')

        # Find the index of the **first** occurrence of the **leftmost** character in hex_str that exists in string
        for i in range(len(hex_str)):
            if hex_str[i] in string:
                index = string.index(hex_str[i])
                result[num] = index
                break

    return result

# Example usage:
arr = [983040, 176, 7, 0, 3]
string = '3b07f'
result = map_array_to_string_index(arr, string)
print(result)