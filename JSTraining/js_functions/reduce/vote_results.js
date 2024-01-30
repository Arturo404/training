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


vote_results_template = {
    potential_voters_18_25: 0,
    voters_18_25: 0,
    potential_voters_26_35: 0,
    voters_26_35: 0,
    potential_voters_36_55: 0,
    voters_36_55: 0
}

function updateVoteResults(current_results, voter) {
    switch(true) {
        case voter.age >= 18 && voter.age <= 25:
            current_results.potential_voters_18_25 += 1;
            if(voter.voted) current_results.voters_18_25 += 1;
            break;
        case voter.age >= 26 && voter.age <= 35:
            current_results.potential_voters_26_35 += 1;
            if(voter.voted) current_results.voters_26_35 += 1;
            break;
        case voter.age >= 36 && voter.age <= 55:
            current_results.potential_voters_36_55 += 1;
            if(voter.voted) current_results.voters_36_55 += 1;
            break;
        default:
    }
    return current_results;
}


function computeVoteResults(array_voters) {
    return array_voters.reduce(updateVoteResults, vote_results_template);
}

console.log(computeVoteResults(array_voters));