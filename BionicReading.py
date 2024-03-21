def uppercase_first_half(input_string):
    # Calculate the midpoint of the string
    midpoint = len(input_string) // 2

    # Convert the first half of the string to uppercase
    modified_string = input_string[:midpoint].upper() + input_string[midpoint:]

    return modified_string

# Example usage:
input_string = input("Enter a string: ")
result = uppercase_first_half(input_string)
print("Modified string:", result)