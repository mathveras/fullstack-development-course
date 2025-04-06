const yearInput = document.getElementById('yearInput');
const checkButton = document.getElementById('checkButton');
const resultDiv = document.getElementById('result');

function isLeapYear(year) {
    return (year % 4 === 0 && year % 100 !== 0) || year % 400 === 0;
}

function handleCheck() {
    const year = parseInt(yearInput.value);
    
    if (isNaN(year)) {
        resultDiv.textContent = 'Please enter a valid year!';
        resultDiv.className = '';
        return;
    }

    if (isLeapYear(year)) {
        resultDiv.textContent = `${year} is a leap year!`;
        resultDiv.className = 'leap';
    } else {
        resultDiv.textContent = `${year} is not a leap year.`;
        resultDiv.className = 'not-leap';
    }
}

checkButton.addEventListener('click', handleCheck);
yearInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') handleCheck();
});
