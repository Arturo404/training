array_strings = ["bawdba", "bAWDPQKWOOibi", "bobo", "dqWDw", "dwdppmn", "erthj"];

function containsVowel(string) {
    const string_lowercase = string.toLowerCase()
    for (const vowel of ["a", "e", "y", "u", "i", "o"]) {
        if(string_lowercase.includes(vowel)) return true;
    }
    return false;
}

function filterWithVowel(array_strings) {
    const array_filtered = array_strings.filter(containsVowel);
    return array_filtered;
}

console.log(filterWithVowel(array_strings));
