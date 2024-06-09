def hex_to_decimal(hex_digit):
    """Converts a single hexadecimal digit to its decimal equivalent."""
    hex_map = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }
    return hex_map[hex_digit.upper()]

def two_digit_hex_to_decimal(hex_string):
    """Converts a two-digit hexadecimal string to its decimal equivalent."""
    return hex_to_decimal(hex_string[0]) * 16 + hex_to_decimal(hex_string[1])

def hex_to_rgb(hex_code):
    """Converts a hexadecimal RGB code to its R, G, B components."""
    if len(hex_code) != 7 or hex_code[0] != '#':
        raise ValueError("Invalid hexadecimal RGB code format.")
    
    red = two_digit_hex_to_decimal(hex_code[1:3])
    green = two_digit_hex_to_decimal(hex_code[3:5])
    blue = two_digit_hex_to_decimal(hex_code[5:7])
    
    return {"R": red, "G": green, "B": blue}

def main():
    print("Hex to RGB")
    while True:
        hex_code = input("Enter the Hexadecimal RGB Code: ")
        if hex_code.lower() in ["quit", "q"]:
            break
        
        try:
            rgb_values = hex_to_rgb(hex_code)
            print("\nRGB Values")
            for key, value in rgb_values.items():
                print(f"{key}: {value}")
            print()
        except ValueError as e:
            print(e)

main()
