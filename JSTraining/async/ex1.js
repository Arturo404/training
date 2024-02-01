import { getRandomInt } from './utils.js';

async function returnAPromise() {
    return new Promise( (resolve)=>{
        setTimeout(()=>{
            resolve(getRandomInt(1,10));
        }, 3000);
    })
}

async function usePromise() {
    console.log(await returnAPromise());
}

returnAPromise().then((result)=>{console.log(result);}).catch((error)=>{console.log(error);});

usePromise();