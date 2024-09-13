def hexadecimal_to_decimal(string):
    string = string.lower()  # Convert the input string to lowercase for consistent processing
    decimal_value = 0
    
    # Define the hexadecimal digit values
    hex_values = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15
    }
    
    # Process the string from right to left, with index i representing the position
    for i, char in enumerate(reversed(string)):
        if char in hex_values:
            value = hex_values[char]
            decimal_value += value * (16 ** i)  # Convert each digit to decimal and sum up
        else:
            raise ValueError(f"Invalid character '{char}' in hexadecimal input")

    return decimal_value

# Test the function
if __name__ == "__main__":
    print(hexadecimal_to_decimal("1A3"))  # Expected output: 419
