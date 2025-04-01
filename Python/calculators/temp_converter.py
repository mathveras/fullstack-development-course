# -- Temperature Converter --- #

""" 
This script converts temperatures between Celsius, Fahrenheit and Kelvin.
"""
print("--- Temperature Converter ---")

print(">>> Celsius to Fahrenheit <<<")
tempC = float(input("Enter temperature in Celsius: "))
tempF = (tempC * 9/5) + 32
print(f"{tempC}°C is equal to {tempF}°F.\n")

print(">>> Celsius to Kelvin <<<")
tempC = float(input("Enter temperature in Celsius: "))
tempK = (tempC + 273.15)
print(f"{tempC}°C is equal to {tempK}K.\n")

print(">>> Fahrenheit to Celsius <<< ")
tempF = float(input("Enter temperature in Fahrenheit: "))
tempC = (tempF - 32) * 5/9
print(f"{tempF}°F is equal to {tempC}°C.\n")

print(">>> Fahrenheit to Kelvin <<<")
tempF = float(input("Enter temperature in Fahrenheit: "))
tempK = (tempF - 32) * 5/9 + 273.15
print(f"{tempF}°F is equal to {tempK}K.\n")

print(">>> Kelvin to Celsius <<<")
tempK = float(input("Enter temperature in Kelvin: "))
tempC = (tempK - 273.15)
print(f"{tempK}K is equal to {tempC}°C.\n")

print(">>> Kelvin to Fahrenheit <<<")
tempK = float(input("Enter temperature in Kelvin: "))
tempF = (tempK - 273.15) * 9/5 + 32
print(f"{tempK}K is equal to {tempF}°F.\n")
