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
    const array_mapped = array_persons.filter((person)=>{
        return person.age>25 && person.age<35
    }).map((person)=>{return person.name});
    return array_mapped;
}

console.log(selectYoungAges(array_persons));