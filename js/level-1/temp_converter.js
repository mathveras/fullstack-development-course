Celsius = parseFloat(prompt('Enter your temperature in Celsius: '))
Fahrenheit = celsiusToFahrenheit(Celsius);

function celsiusToFahrenheit(Celsius){
    Fahrenheit = (Celsius * 9/5) + 32;
    return Fahrenheit;
}

alert(`${Celsius}°C is equal to ${Fahrenheit}°F`);
