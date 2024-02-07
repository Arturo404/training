import { getRandomInt } from './utils.js';

const makePromises = (num_promises) => {
    let array_promises = [];
    for(let i=0; i<num_promises; i++) {
        array_promises.push(new Promise( (resolve)=>{
            const random_value = getRandomInt(0, 10);
            setTimeout(()=>{
                resolve(`Promise number ${i} resolved after ${random_value} seconds.`);
            }, random_value*1000);
        }));
    }
    return array_promises;
}


const usingThen = () => {
    Promise.all(makePromises(10)).then(results=>{console.log("Unsing then: ", results);});
}

const usingAwait = async () => {
    console.log("Using await: ");
    try {
        console.log(await Promise.all(makePromises(10)));
    }
    catch(err) {
        console.log(err.message);
    }
}

const usingThen_o = false;
if(usingThen_o) {
    usingThen();
}
else {
    usingAwait();
}
