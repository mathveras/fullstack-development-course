year = (prompt('Enter a number: '));

function leapY(year){
    return(year % 4 === 0 && year % 100 !== 0) || year % 400 === 0;
}

if(leapY(year)){
    alert(`${year} is a leap year.`);
}
else {
    alert(`${year} is not a leap year.`);
}
