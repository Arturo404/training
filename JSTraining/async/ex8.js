
const utils = require('./utils');

function arrayOfRandomPromises(num_promises) {
    let array_promises = [];
    for(let i=0; i<num_promises; i++) {
        array_promises.push(new Promise( (resolve, reject)=>{
            const random_value = utils.getRandomInt(0, 2);
            setTimeout(()=>{
                if (random_value==0) reject(new Error(`Promise ${i} rejected because value is ${random_value}`));
                else resolve(`Promise ${i} resolved because value is ${random_value}`);
            }, 2*1000);
        }));
    }

    Promise.all(array_promises).then((result)=>{console.log(result);}, (error)=>{console.log(error.message);});
}

arrayOfRandomPromises(10);