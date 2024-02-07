import { sumUntilNumber } from './utils.js';

const returnAPromise = (num) => {
    return new Promise( (resolve)=>{
        setTimeout(()=>{
            resolve(sumUntilNumber(num));
        }, 5000);
    });
}

const usePromise = async (num) => {
    console.log(await returnAPromise(num));
}

returnAPromise(4).then((result)=>{console.log(result);});

usePromise(5);