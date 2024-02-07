import { getRandomInt } from './utils.js';

const returnAPromise = () => {
    return new Promise( (resolve)=>{
        setTimeout(()=>{
            resolve(getRandomInt(1,10));
        }, 3000);
    })
}

const usePromise = async () => {
    console.log(await returnAPromise());
}

returnAPromise().then((result)=>{console.log(result);}).catch((error)=>{console.log(error);});

usePromise();