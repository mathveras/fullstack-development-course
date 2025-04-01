raio = parseFloat(prompt('Type the radius of the circle: '));

if(!isNaN(raio)){
    area = Math.PI * Math.pow(raio, 2);
    alert(`The circle area is: ${area}`);
}
else{
    alert('Please, enter a valid number for the radius.');
}

result = document.getElementById('result');
result.textContent = `The circle radius is: ${area.toFixed(2)}`;
