const inputsContainer = document.getElementById('inputs-container');
const addInputBtn = document.getElementById('addInputBtn');
const compareBtn = document.getElementById('compareBtn');
const clearBtn = document.getElementById('clearBtn');
const basicResult = document.getElementById('basicResult');
const ascendingResult = document.getElementById('ascendingResult');
const descendingResult = document.getElementById('descendingResult');

const MAX_INPUTS = 10;
let inputCount = 2;

function addInputField() {
    if (inputCount >= MAX_INPUTS) {
        alert(`Maximum of ${MAX_INPUTS} numbers reached`);
        return;
    }
    
    const newInputGroup = document.createElement('div');
    newInputGroup.className = 'input-group';
    newInputGroup.innerHTML = `
        <input type="number" placeholder="Enter another number" class="number-input">
        <button class="remove-btn">×</button>
    `;
    inputsContainer.appendChild(newInputGroup);
    inputCount++;
    
    newInputGroup.querySelector('.remove-btn').addEventListener('click', () => {
        inputsContainer.removeChild(newInputGroup);
        inputCount--;
    });
}

function displayNumberList(numbers, element, sortOrder = 'asc') {
    element.innerHTML = '';
    const sorted = [...numbers].sort((a, b) => sortOrder === 'asc' ? a - b : b - a);
    
    sorted.forEach(num => {
        const chip = document.createElement('span');
        chip.className = 'number-chip';
        chip.textContent = num;
        element.appendChild(chip);
    });
}

function compareAllNumbers() {
    const inputs = document.querySelectorAll('.number-input');
    const numbers = [];
    
    for (const input of inputs) {
        const num = parseFloat(input.value);
        if (!isNaN(num)) numbers.push(num);
    }
    
    if (numbers.length < 2) {
        basicResult.textContent = "Please enter at least 2 valid numbers!";
        basicResult.style.backgroundColor = "#fff3cd";
        ascendingResult.innerHTML = '';
        descendingResult.innerHTML = '';
        return;
    }
    
    const max = Math.max(...numbers);
    const min = Math.min(...numbers);
    
    if (max === min) {
        basicResult.textContent = `All ${numbers.length} numbers are equal (${max})`;
    } else {
        basicResult.textContent = `Highest: ${max} | Lowest: ${min} | Total numbers: ${numbers.length}`;
    }
    basicResult.style.backgroundColor = "#d4edda";
    
    displayNumberList(numbers, ascendingResult, 'asc');
    displayNumberList(numbers, descendingResult, 'desc');
}

function clearAll() {
    document.querySelectorAll('.number-input').forEach(input => {
        input.value = '';
    });
    basicResult.textContent = "Enter at least 2 numbers to compare";
    basicResult.style.backgroundColor = "#f8f9fa";
    ascendingResult.innerHTML = '';
    descendingResult.innerHTML = '';
}

addInputBtn.addEventListener('click', addInputField);
compareBtn.addEventListener('click', compareAllNumbers);
clearBtn.addEventListener('click', clearAll);

inputsContainer.addEventListener('keypress', (e) => {
    if (e.target.classList.contains('number-input') && e.key === 'Enter') {
        compareAllNumbers();
    }
});
