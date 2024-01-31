const utils = require('./utils');

function makePromises(num_promises) {
    let array_promises = [];
    for(let i=0; i<num_promises; i++) {
        array_promises.push(new Promise( (resolve)=>{
            const random_value = utils.getRandomInt(0, 10);
            setTimeout(()=>{
                resolve(`Promise number ${i} resolved after ${random_value} seconds.`);
            }, random_value*1000);
        }));
    }
    return array_promises;
}

Promise.all(makePromises(10)).then(result=>{console.log(result);});
