import { getRandomInt } from './utils.js';

const returnPromiseThatReturnPromise = () => {
    return new Promise((resolve)=>{
        setTimeout(()=>{
            resolve(new Promise((resolve)=>{
                setTimeout(()=>{
                    resolve(getRandomInt(1,10));
                }, 10*1000);
            }));
        }, 5*1000);
    });
}


const usingThen = () => {
    console.log("Using then: ");
    returnPromiseThatReturnPromise().then((result)=>{console.log(result);});
}

const usingAwait = async () => {
    console.log("Using await: ");
    try {
        const promise = await returnPromiseThatReturnPromise();
        console.log(await promise);
    }
    catch(err) {
        console.log(err.message);
    }
}

const usingThen_o = true;
if(usingThen_o) {
    usingThen();
}
else {
    usingAwait();
}