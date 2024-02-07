array_numbers = [23,-1,234,-11,-45,66,-214,24,677];

const selectPositiveAndSquare = (array_numbers) => {
    const array_mapped = array_numbers.filter((number)=>{
        return number > 0;
    }).map((number)=>{
        return number**2;
    });
    return array_mapped;
}

console.log(selectPositiveAndSquare(array_numbers));