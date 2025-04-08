"""
    Auxiliary file for 'temp_converter-2.py' for better organization.
"""
def handle_retry() -> bool | None:
    """Helper function to handle retry logic for all functions.
    
    Returns:
        bool | None: True to retry, False to exit, None to return to main menu
    """
    while True:
        choice = input("\nWhat would you like to do?\n[R] Retry \n[X] Exit\n[M] Return to menu\nChoice: ").strip().upper()
        if choice in ["R", "X", "M"]:
            return True if choice == "R" else (None if choice == "M" else False)
        print("❌ Please enter R, X, or M")


def celsius_to_fahrenheit() -> bool | None:
    """Function to convert Celsius to Fahrenheit. (°F = (°C * 9/5) + 32)

    Returns:
        bool | None: True to retry, False to exit, None to return to main menu
    """
    while True:
        print("\033[H\033[J", end="")
        print("\n>>> Celsius to Fahrenheit <<<")
        while True:
            try:
                tempC = float(input("Enter the temperature in Celsius: "))
                break
            except ValueError:
                print("\n❌ Please, only enter numbers!\n")

        tempF = (tempC * 9/5) + 32
        print(f"{tempC}°C is equal to {tempF}°F.\n")

        retry = handle_retry()
        if retry is not True:
            return retry


def celsius_to_kelvin() -> bool | None:
    """Function to convert Celsius to Kelvin. K = °C + 273.15

    Returns:
        bool | None: True to retry, False to exit, None to return to main menu
    """
    while True:
        print("\033[H\033[J", end="")
        print("\n>>> Celsius to Kelvin <<<")
        while True:
            try:
                tempC = float(input("Enter the temperature in Celsius: "))
                break
            except ValueError:
                print("\n❌ Please, only enter numbers!\n")

        tempK = (tempC + 273.15)
        print(f"{tempC}°C is equal to {tempK}K.\n")

        retry = handle_retry()
        if retry is not True:
            return retry


def fahrenheit_to_celsius() -> bool | None:
    """Function to convert Fahrenheit to Celsius. (°C = (°F - 32) * 5/9)

    Returns:
        bool | None: True to retry, False to exit, None to return to main menu
    """
    while True:
        print("\033[H\033[J", end="")
        print("\n>>> Fahrenheit to Celsius <<< ")

        while True:
            try:
                tempF = float(input("Enter the temperature in Fahrenheit: "))
                break
            except ValueError:
                print("\n❌ Please, only enter numbers!\n")

        tempC = (tempF - 32) * 5/9
        print(f"{tempF}°F is equal to {tempC}°C.\n")

        retry = handle_retry()
        if retry is not True:
            return retry


def fahrenheit_to_kelvin() -> bool | None:
    """Function to convert Fahrenheit to Kelvin. (K = (°F - 32) * 5/9 + 273.15)

    Returns:
        bool | None: True to retry, False to exit, None to return to main menu
    """
    while True:
        print("\033[H\033[J", end="")
        print("\n>>> Fahrenheit to Kelvin <<<")
        while True:
            try:
                tempF = float(input("Enter the temperature in Fahrenheit: "))
                break
            except ValueError:
                print("\n❌ Please, only enter numbers!\n")

        tempK = (tempF - 32) * 5/9 + 273.15
        print(f"{tempF}°F is equal to {tempK}K.\n")

        retry = handle_retry()
        if retry is not True:
            return retry


def kelvin_to_celsius() -> bool | None:
    """Function to convert Kelvin to Celsius. (°C = K - 273.15)
    
    Returns:
        bool | None: True to retry, False to exit, None to return to main menu
    """
    while True:
        print("\033[H\033[J", end="")
        print("\n>>> Kelvin to Celsius <<<")
        while True:
            try:
                tempK = float(input("Enter the temperature in Kelvin: "))
                break
            except ValueError:
                print("\n❌ Please, only enter numbers!\n")

        tempC = (tempK - 273.15)
        print(f"{tempK}K is equal to {tempC}°C.\n")

        retry = handle_retry()
        if retry is not True:
            return retry


def kelvin_to_fahrenheit() -> bool | None:
    """Function to convert Kelvin to Fahrenheit. (°F = (K - 273.15) * 9/5 + 32)

    Returns:
        bool | None: True to retry, False to exit, None to return to main menu
    """
    while True:
        print("\033[H\033[J", end="")
        print("\n>>> Kelvin to Fahrenheit <<<")
        while True:
            try:
                tempK = float(input("Enter the temperature in Kelvin: "))
                break
            except ValueError:
                print("\n❌ Please, only enter numbers!\n")

        tempF = (tempK - 273.15) * 9/5 + 32
        print(f"{tempK}K is equal to {tempF}°F.\n")

        retry = handle_retry()
        if retry is not True:
            return retry
