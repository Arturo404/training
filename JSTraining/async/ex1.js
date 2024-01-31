const utils = require('./utils');

async function returnAPromise() {
    return new Promise( (resolve)=>{
        setTimeout(()=>{
            resolve(utils.getRandomInt(1,10));
        }, 3000);
    })
}

async function usePromise() {
    console.log(await returnAPromise());
}

returnAPromise().then((result)=>{console.log(result);}).catch((error)=>{console.log(error);});

usePromise();