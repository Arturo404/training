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
    return voter.voted? count_voters+1 : count_voters;
}

const countVoters = (array_voters) => {
    return array_voters.reduce(addVoter, 0);
}