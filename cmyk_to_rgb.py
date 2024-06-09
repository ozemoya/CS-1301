def CMYK_to_RGB(cmyk_dict):
   
    C, M, Y, K = cmyk_dict['C'], cmyk_dict['M'], cmyk_dict['Y'], cmyk_dict['K']
    R = 255 * (1 - C / 100) * (1 - K / 100)
    G = 255 * (1 - M / 100) * (1 - K / 100)
    B = 255 * (1 - Y / 100) * (1 - K / 100)

    return {
        'R': int(R),
        'G': int(G),
        'B': int(B)
    }

def main():
    print("CMYK To RGB Converter")
    while True:
        cyan_input = input("Enter the Cyan Color Value or 'quit'/'q' to exit: ")
        
        if cyan_input.lower() in ['quit', 'q']:
            break
        
        try:
            cyan = float(cyan_input)
            magenta = float(input("Enter the Magenta Color Value: "))
            yellow = float(input("Enter the Yellow Color Value: "))
            key = float(input("Enter the Key Color Value: "))

            rgb_dict = CMYK_to_RGB({'C': cyan, 'M': magenta, 'Y': yellow, 'K': key})

            print(f"RGB Values:\nRed: {rgb_dict['R']}\nGreen: {rgb_dict['G']}\nBlue: {rgb_dict['B']}")

        except ValueError:
            print("Please enter valid numbers for CMYK values.")

if __name__ == "__main__":
    main()
