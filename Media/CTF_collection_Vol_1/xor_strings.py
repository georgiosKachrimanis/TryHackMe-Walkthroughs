def xor_strings(s1, s2):
    """XOR two strings and return the hexadecimal result."""
    int_s1 = int(s1, 16)
    int_s2 = int(s2, 16)
    xor_result = int_s1 ^ int_s2
    return format(xor_result, 'x')

def hex_to_ascii(hex_str):
    """Convert a hexadecimal string to an ASCII string."""
    ascii_str = bytes.fromhex(hex_str).decode('utf-8', errors='ignore')
    return ascii_str

# Define the two strings
s1 = "44585d6b2368737c65252166234f20626d"
s2 = "1010101010101010101010101010101010"

# Get the XOR result
result = xor_strings(s1, s2)

# Convert the XOR result to ASCII and print it
ascii_result = hex_to_ascii(result)
print(f"The XOR of S1 and S2 in ASCII is: {ascii_result}")
