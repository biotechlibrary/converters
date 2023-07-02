def numeral_to_binary(numeral):
    try:
        decimal = int(numeral)
        binary = bin(decimal)[2:]
        return binary
    except ValueError:
        return "Invalid numeral"

# Example usage
numeral = input("Enter a numeral: ")
binary = numeral_to_binary(numeral)
print("Binary representation:", binary)
