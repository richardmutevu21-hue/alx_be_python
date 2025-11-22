FAHRENHEIT_TO_CELSIUS_FACTOR = 5.0 / 9.0
CELSIUS_TO_FAHRENHEIT_FACTOR = 9.0 / 5.0

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global factor.
    Expects a numeric value (int/float). Raises ValueError on invalid input.
    """
    try:
        f = float(fahrenheit)
    except (TypeError, ValueError):
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    # formula: (F - 32) * 5/9
    return (f - 32.0) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global factor.
    Expects a numeric value (int/float). Raises ValueError on invalid input.
    """
    try:
        c = float(celsius)
    except (TypeError, ValueError):
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    # formula: C * 9/5 + 32
    return c * CELSIUS_TO_FAHRENHEIT_FACTOR + 32.0

def main():
    raw_temp = input("Enter the temperature to convert: ").strip()
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    try:
        if unit == "F":
            c = convert_to_celsius(raw_temp)
            print(f"{float(raw_temp)}°F is {c}°C")
        elif unit == "C":
            f = convert_to_fahrenheit(raw_temp)
            print(f"{float(raw_temp)}°C is {f}°F")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()