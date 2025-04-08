# --- Ternary Operators 2 --- #

""" 
A ternary operator is a shorthand way of writing an if-else statement in Python.
It allows you to assign a value to a variable based on a condition in a single line of code.

This is a slighly improved version from the simple version 'ternary_operator.py'

The syntax is as follows:
    variable = value_if_true if condition else value_if_false
"""
from operators import (
    check_age_majority,
    check_even_odd,
    upper_or_lower,
    test_your_precision,
)

def operator_selector() -> int:
    """This function clears the terminal and displays a menu with options for different operators.
    
    Returns:
        int: The integer number that will select what operator to use.
    """
    print("\033[H\033[J", end="")
    print("\n--- Ternary Operators 2 ---")

    print("\n1. 🔞 Check Age Majority")
    print("2. ❓ Even or Odd")
    print("3. ⬆️  Uppercase or Lowercase ⬇️")
    print("4. 🎯 Test Your Precision")
    print("0. 🚪 Exit")

    while True:
        try:
            selector = int(input("\n Select an option (0-4): "))
            if 0 <= selector <= 4:
                return selector
            else:
                print("Please, enter a valid option! (0-4)")
        except ValueError:
            print("Please, only enter integer numbers!")


def run_selected(selector: int) -> bool:
    """Function that runs the user selected operator.

    Args:
        selector (int): The integer number that represents what operator was selected.

    Returns:
        bool: True if the user selected an operator or False if exited the script.
    """
    if selector == 0:
        print("\nGoodbye! 👋")
        return False

    operators = {
        1: check_age_majority,
        2: check_even_odd,
        3: upper_or_lower,
        4: test_your_precision
    }

    result = operators[selector]()
    return True if result is None else result


def main():
    while True:
        selector = operator_selector()
        if not run_selected(selector):
            break

if __name__ == "__main__":
    main()
