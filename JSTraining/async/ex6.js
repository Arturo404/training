const returnAFailedPromise = () => {
    return new Promise( (resolve, reject)=>{
        reject(new Error("FAILED"));
    });
}


const usingThen = () => {
    console.log("Using then: ");
    returnAFailedPromise().then(result=>{console.log(result);}).catch(error=>{console.log(error.message);});
}

const usingAwait = async () => {
    console.log("Using await: ");

    try {
        console.log(await returnAFailedPromise());
    }
    catch(err) {
        console.log(err.message);
    }
}

const usingThen_o = false;
if(usingThen_o) {
    usingThen();

}
else {
    usingAwait();
}

