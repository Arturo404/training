function getRandomInt(min,max) {
    return Math.floor(Math.random() * (max - min) ) + min;
}

function sumUntilNumber(num) {
    return (num*(num+1))/2;
}

exports.getRandomInt = getRandomInt;
exports.sumUntilNumber = sumUntilNumber;