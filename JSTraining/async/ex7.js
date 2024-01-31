const utils = require('./utils');

function returnPromiseThatReturnPromise() {
    return new Promise((resolve)=>{
        setTimeout(()=>{
            resolve(new Promise((resolve)=>{
                setTimeout(()=>{
                    resolve(utils.getRandomInt(1,10));
                }, 10*1000);
            }));
        }, 5*1000);
    });
}

async function usePromise() {
    const promise = await returnPromiseThatReturnPromise();
    console.log(await promise);
}


returnPromiseThatReturnPromise().then((result)=>{console.log(result);});


usePromise();