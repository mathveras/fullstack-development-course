"""
    Auxiliary file for 'temp_converter-2.py' for better organization.
"""
def check_continue(retry: str) -> bool:
    """Helper function to check if the User wants to continue to the Temperature Converter.

    Args:
        retry (str): User input Y (yes) or N (no).

    Returns:
        bool: Y to continue to Temperature Converter or N to close the Temperature Converter.
    """
    while True:
        if retry == "Y":
            return True
        elif retry == "N":
            print("Goodbye! 👋")
            return False
        else:
            retry = input("Please enter Y or N: ")


def celsius_to_fahrenheit():
    print("\n>>> Celsius to Fahrenheit <<<")
    tempC = float(input("Enter temperature in Celsius: "))
    tempF = (tempC * 9/5) + 32
    print(f"{tempC}°C is equal to {tempF}°F.\n")

    retry = input("Continue? (Y/N): ").strip().upper()
    return check_continue(retry)


def celsius_to_kelvin():
    print("\n>>> Celsius to Kelvin <<<")
    tempC = float(input("Enter a temperature in Celsius: "))
    tempK = (tempC + 273.15)
    print(f"{tempC}°C is equal to {tempK}K.\n")

    retry = input("Continue? (Y/N): ").strip().upper()
    return check_continue(retry)


def fahrenheit_to_celsius():
    print("\n>>> Fahrenheit to Celsius <<< ")
    tempF = float(input("Enter temperature in Fahrenheit: "))
    tempC = (tempF - 32) * 5/9
    print(f"{tempF}°F is equal to {tempC}°C.\n")

    retry = input("Continue? (Y/N): ").strip().upper()
    return check_continue(retry)


def fahrenheit_to_kelvin():
    print("\n>>> Fahrenheit to Kelvin <<<")
    tempF = float(input("Enter temperature in Fahrenheit: "))
    tempK = (tempF - 32) * 5/9 + 273.15
    print(f"{tempF}°F is equal to {tempK}K.\n")

    retry = input("Continue? (Y/N): ").strip().upper()
    return check_continue(retry)


def kelvin_to_celsius():
    print("\n>>> Kelvin to Celsius <<<")
    tempK = float(input("Enter temperature in Kelvin: "))
    tempC = (tempK - 273.15)
    print(f"{tempK}K is equal to {tempC}°C.\n")

    retry = input("Continue? (Y/N): ").strip().upper()
    return check_continue(retry)


def kelvin_to_fahrenheit():
    print("\n>>> Kelvin to Fahrenheit <<<")
    tempK = float(input("Enter temperature in Kelvin: "))
    tempF = (tempK - 273.15) * 9/5 + 32
    print(f"{tempK}K is equal to {tempF}°F.\n")

    retry = input("Continue? (Y/N): ").strip().upper()
    return check_continue(retry)
