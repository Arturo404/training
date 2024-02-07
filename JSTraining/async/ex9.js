const printHelloWorld = () => {
    console.log("Hello World!");
}

const stoppingPromise = (interval_id) => {
    return new Promise((resolve)=>{
        setTimeout(()=>{
            clearInterval(interval_id);
            resolve();
        }, 10*1000);
    });
}

const createAndClearIntervalUsingThen = () => {
    console.log("Using then: ");
    const interval_id = setInterval(printHelloWorld, 1*1000);
    stoppingPromise(interval_id).then((result)=>{}).catch((err)=>{console.log(err);});
}

const createAndClearIntervalUsingAwait = async () => {
    console.log("Using await: ");
    const interval_id = setInterval(printHelloWorld, 1*1000);
    await stoppingPromise(interval_id);
}

const usingThen_o = false;
if(usingThen_o) {
    createAndClearIntervalUsingThen();
}
else {
    createAndClearIntervalUsingAwait();
}
