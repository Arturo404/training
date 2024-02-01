function printHelloWorld() {
    console.log("Hello World!");
}

function stoppingPromise(interval_id) {
    return new Promise((resolve)=>{
        setTimeout(()=>{
            clearInterval(interval_id);
            resolve();
        }, 10*1000);
    });
}

async function createAndClearIntervalUsingThen() {
    console.log("Using then: ");
    const interval_id = setInterval(printHelloWorld, 1*1000);
    stoppingPromise(interval_id).then((result)=>{}).catch((err)=>{console.log(err);});
}

async function createAndClearIntervalUsingAwait() {
    console.log("Using await: ");
    const interval_id = setInterval(printHelloWorld, 1*1000);
    await stoppingPromise(interval_id);
}

/*
async function createAndClearInterval() {
    interval_id = setInterval(printHelloWorld, 1*1000);
    await new Promise((resolve)=>{
        setTimeout(()=>{
            clearInterval(interval_id);
            resolve();
        }, 10*1000);
    })
}
*/

const usingThen_o = false;
if(usingThen_o) {
    createAndClearIntervalUsingThen();
}
else {
    createAndClearIntervalUsingAwait();
}
