array_voters = [
    {
        name: "Bob",
        age: 30,
        voted: true
    },
    {
        name: "Jake",
        age: 32,
        voted: true
    },
    {
        name: "Kate",
        age: 25,
        voted: false
    },
    {
        name: "Sam",
        age: 20,
        voted: false
    },
    {
        name: "Phil",
        age: 21,
        voted: true
    },
    {
        name: "Ed",
        age: 25,
        voted: true
    },
    {
        name: "Tamil",
        age: 54,
        voted: true
    },
    {
        name: "Mary",
        age: 31,
        voted: false
    }
];

const addVoter = (count_voters, voter) => {
    const new_count = voter.voted? count_voters+1 : count_voters;
    return new_count;
}

const countVoters = (array_voters) => {
    const num_voters = array_voters.reduce(addVoter, 0);
    return num_voters;
}

console.log(countVoters(array_voters));