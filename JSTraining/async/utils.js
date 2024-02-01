export function getRandomInt(min,max) {
    return Math.floor(Math.random() * (max - min) ) + min;
}

export function sumUntilNumber(num) {
    return (num*(num+1))/2;
}

export async function successfulPromise(res) {
    return new Promise(resolve=>{resolve(res);});
}

export async function failedPromise(err) {
    try {
        return new Promise((resolve,reject)=>{
            reject(err);
        });
    }
    catch(err) {
        console.log("mama");
    }
}


