import { sumUntilNumber } from './utils.js';

async function returnAPromise(num) {
    return new Promise( (resolve)=>{
        setTimeout(()=>{
            resolve(sumUntilNumber(num));
        }, 5000);
    });
}

async function usePromise(num) {
    console.log(await returnAPromise(num));
}

returnAPromise(4).then((result)=>{console.log(result);});

usePromise(5);