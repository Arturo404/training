import { getRandomInt } from './utils.js';

function arrayOfRandomPromises(num_promises) {
    let array_promises = [];
    for(let i=0; i<num_promises; i++) {
        array_promises.push(new Promise( (resolve, reject)=>{
            const random_value = getRandomInt(0, 2);
            setTimeout(()=>{
                if (random_value==0) reject(new Error(`Promise ${i} rejected because value is ${random_value}`));
                else resolve(`Promise ${i} resolved because value is ${random_value}`);
            }, 10*1000);
        }));
    }

    return Promise.all(array_promises);
}

function usingThen(num_promises) {
    console.log("Using then: ");
    arrayOfRandomPromises(num_promises)
        .then((result)=>{console.log(result);}, (error)=>{console.log(error.message);})
        .catch((err)=>{console.log(err.message);});
}

async function usingAwait(num_promises) {
    console.log("Using await: ");
    try {
        console.log(await arrayOfRandomPromises(num_promises));
    }
    catch(err) {
        console.log(err.message);
    }
}

const usingThen_o = true;
const num_promises = 10;
if(usingThen_o) {
    usingThen(num_promises);
}
else {
    usingAwait(num_promises);
}