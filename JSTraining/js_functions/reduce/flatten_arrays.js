array_arrays = [
    ["1", "2", "3"],
    [true],
    [4,5,6]
];

function addArray(flat_array, array) {
    return flat_array.concat(array);
}

function flattenArrays(array_arrays) {
    const flat_array = array_arrays.reduce(addArray);
    return flat_array;
}

console.log(flattenArrays(array_arrays));