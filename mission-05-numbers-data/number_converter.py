"""
Digital Detective - Mission 5: Number Converter
Interactive script that converts a positive decimal integer into binary and hexadecimal representations.
"""

def main():
    print("=" * 45)
    print("   Digital Detective: Number Converter")
    print("=" * 45)
    
    user_input = input("Enter a positive decimal integer: ").strip()
    
    try:
        decimal_val = int(user_input)
        if decimal_val < 0:
            print("Error: Please enter a positive integer.")
            return
            
        binary_val = bin(decimal_val)          # e.g., '0b101010'
        hex_val = hex(decimal_val).upper()     # e.g., '0X2A'
        # Format clean uppercase hex with standard prefix
        clean_hex = "0x" + hex(decimal_val)[2:].upper()
        
        print("
--- Conversion Results ---")
        print(f"Decimal (Base 10)     : {decimal_val}")
        print(f"Binary (Base 2)       : {binary_val}  (Raw: {bin(decimal_val)[2:]})")
        print(f"Hexadecimal (Base 16) : {clean_hex}  (Raw: {hex(decimal_val)[2:].upper()})")
        print("=" * 45)
    except ValueError:
        print("Error: Invalid input. Please enter a valid decimal number.")

if __name__ == "__main__":
    main()
