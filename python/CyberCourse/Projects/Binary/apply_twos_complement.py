def decimal_to_binary(decimal, bit_width):
    binary = bin(decimal)[2:]
    binary = binary.zfill(bit_width)
    return binary


def apply_twos_complement(binary, bit_width):
    inverted = ''.join("1" if bit == "0" else "0" for bit in binary)
    reverse_decimal = int(inverted, 2) + 1
    return decimal_to_binary(reverse_decimal, bit_width)

try:
    decimal = int(input("Enter decimal number:"))
    bit_width = int(input("Enter amount of bits:"))

    binary = decimal_to_binary(decimal, bit_width)
    print("Binary:", binary)

    inverted = apply_twos_complement(binary, bit_width)
    print("-" + str(decimal) + " -> " + inverted)
    
except Exception as e:
    print("Error:", e)
    print("Please enter valid integers.")

