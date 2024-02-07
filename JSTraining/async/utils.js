export function getRandomInt(min,max) {
    return Math.floor(Math.random() * (max - min) ) + min;
}

export function sumUntilNumber(num) {
    return (num*(num+1))/2;
}

export const successfulPromise = (res) => {
    return new Promise(resolve=>{resolve(res);});
}

export const failedPromise = (err) => {
    try {
        return new Promise((resolve,reject)=>{
            reject(err);
        });
    }
    catch(err) {
        console.log(err.message);
    }
}


