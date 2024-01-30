array_persons = [
    {
        name: "John",
        age: 30
    },
    {
        name: "Alice",
        age: 25
    },
    {
        name: "Itai",
        age: 21
    },
    {
        name: "Nadav",
        age: 21
    }
];

function personToLabel(person) {
    return {label: `${person.name} - ${person.age} years old`};
}

function mapToLabel(array_persons) {
    const array_mapped = array_persons.map(personToLabel);
    return array_mapped;
}

console.log(mapToLabel(array_persons));