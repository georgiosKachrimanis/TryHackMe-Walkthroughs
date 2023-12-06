def decimal_to_hex_to_ascii(decimal_number):
    try:
        # Convert the decimal to hex
        hex_number = hex(decimal_number)[2:] # Removing the '0x' prefix
        
        # If the hex number length is odd, add a leading zero
        if len(hex_number) % 2 != 0:
            hex_number = '0' + hex_number
        
        # Convert hex to ASCII
        ascii_string = ''.join([chr(int(hex_number[i:i+2], 16)) for i in range(0, len(hex_number), 2)])
        
        print(f"Decimal: {decimal_number}")
        print(f"Hexadecimal: {hex_number}")
        print(f"ASCII: {ascii_string}")
        
    except ValueError as e:
        print(f"An error occurred: {e}")
        print("Ensure the hex number corresponds to valid ASCII characters.")

# Take input from the user
decimal_input = int(581695969015253365094191591547859387620042736036246486373595515576333693)
decimal_to_hex_to_ascii(decimal_input)
