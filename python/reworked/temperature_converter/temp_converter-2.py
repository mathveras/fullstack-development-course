# --- Temperature Converter 2 --- #

""" 
This script converts temperatures between Celsius, Fahrenheit and Kelvin. 

This is an slighly improved version from the simple version 'temp_converter.py'
"""
from convertions import(
    celsius_to_fahrenheit,
    celsius_to_kelvin,
    fahrenheit_to_celsius,
    fahrenheit_to_kelvin,
    kelvin_to_celsius,
    kelvin_to_fahrenheit
)


def temp_selector() -> int:
    """Function for the User to select which temperature conversion to use.

    Returns:
        int: The integer number that will select what conversion to use.
    """
    print("--- Temperature Converter 2 ---")

    print("\n1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Fahrenheit to Celsius")
    print("4. Fahrenheit to Kelvin")
    print("5. Kelvin to Celsius")
    print("6. Kelvin to Fahrenheit")
    print("0. Exit")

    while True:
        try:
            selector = (int(input("\nSelect an option (0-6): ")))
            if 0 <= selector <= 6:
                return selector
            else:
                print("Please, enter a valid option! (0-6)")
        except ValueError:
            print("Please, only enter integer numbers!")


def run_selected(selector: int) -> bool:
    """Function that runs the User select converter.

    Args:
        selector (int): The integer number that represents what temperature converter was selected.

    Returns:
        bool: True if the user selected a temperature converter or False if exited the script.
    """
    if selector == 0:
        print("Goodbye! 👋")
        return False
    
    conversion_functions = {
        1: celsius_to_fahrenheit,
        2: celsius_to_kelvin,
        3: fahrenheit_to_celsius,
        4: fahrenheit_to_kelvin,
        5: kelvin_to_celsius,
        6: kelvin_to_fahrenheit
    }

    return conversion_functions[selector]()


def main():
    while True:
        selector = temp_selector()
        if not run_selected(selector):
            break

if __name__ == "__main__":
    main()
