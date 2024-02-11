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

const selectYoungAges = (array_persons) => {
    return array_persons.filter(person=>person.age>25 && person.age<35).map(person=>person.name);
}