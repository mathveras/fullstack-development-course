factorial = prompt('Enter a number: ')

for (index = factorial; index > 0; index--){
    workAround = factorial -= 1;
    workAround *= index;
    alert(factorial * workAround)
}
