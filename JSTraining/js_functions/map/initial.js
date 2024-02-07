array_names = ["John Doe", "Jane Smith", "Itai Cohen", "Nadav Glazer"];

const initials = (full_name) => {
    const names = full_name.split(" ");
    const firstName = names[0], lastName = names[1];
    const initials = `${firstName.charAt(0).toUpperCase()}${lastName.charAt(0).toUpperCase()}`;
    return initials;
}

const  mapToInitials = (array_names) => {
    const array_mapped = array_names.map(initials)
    return array_mapped;
}

console.log(mapToInitials(array_names));