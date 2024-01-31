const utils = require('./utils');
  
async function returnAFailedPromise() {
    return new Promise( (resolve, reject)=>{
        reject(new Error("FAILED"));
    });
}

async function usePromise() {
    try {
        console.log(await returnAFailedPromise());
    }
    catch(err) {
        console.log(err.message);
    }
    
}

returnAFailedPromise().then(result=>{console.log(result);}).catch(error=>{console.log(error.message);});

usePromise();