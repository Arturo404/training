const utils = require('./utils');
  
async function returnAPromise() {
    return new Promise( (resolve, reject)=>{
        setTimeout(()=>{
            const value = utils.getRandomInt(50,100);
            if(value>85) reject(new Error("Number is too big, bigger than 85"));
            resolve(value);
        }, 3000);
    })
}

async function usePromise() {
    try {
        console.log(await returnAPromise());
    }
    catch(err) {
        console.log(err.message);
    }
    
}

returnAPromise().then(result=>{console.log(result);}).catch(error=>{console.log(error.message);});

usePromise();