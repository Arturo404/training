array_strings = ["a","b","c","a","c","s","d","w","f"];

const isUnique = (string, index, array) => {
    let cnt = 0;
    for(const element of array) {
        if(string == element) cnt++;
    }
    if(cnt >= 2) return false;
    return true;
}

const SelectAndMapToUppercase = (array_strings) => {
    const array_mapped = array_strings.filter(isUnique).map((string)=>{return string.toUpperCase()});
    return array_mapped;
}

console.log(SelectAndMapToUppercase(array_strings));