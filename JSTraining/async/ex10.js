import { successfulPromise, failedPromise } from "./utils.js";

async function checkSuccess(promise1, promise2) {
    return Promise.all([promise1,promise2]);
}

function usingThen() {
    console.log("Using then: ");
    checkSuccess(successfulPromise(), failedPromise(new Error("Hahaha I made you fail")))
    .then((res)=>{console.log("success, fail -> success")}, (err)=>{console.log("success, fail -> fail",err.message)});

    checkSuccess(failedPromise(new Error("Hahaha I made you fail")), successfulPromise())
        .then((res)=>{console.log("fail, success -> success")}, (err)=>{console.log("fail, success -> fail", err.message)});

    checkSuccess(failedPromise(new Error("Hahaha I made you fail")), failedPromise(new Error("Hahaha I made you fail")))
        .then((res)=>{console.log("fail, fail -> success")}, (err)=>{console.log("fail, fail -> fail", err.message)});

    checkSuccess(successfulPromise(), successfulPromise())
    .then((res)=>{console.log("success, success -> success")}, (err)=>{"success, success -> fail", console.log(err.message)});
}

async function usingAwait() {
    console.log("Using await: ");
    try {
        await checkSuccess(successfulPromise(), failedPromise(new Error("Hahaha I made you fail")));
        console.log("success, fail -> success");
    }
    catch(err) {
        console.log("success, fail -> fail", console.error(err.message));
    }

    try {
        await checkSuccess(failedPromise(new Error("Hahaha I made you fail")), successfulPromise());
        console.log("fail, success -> success");
    }
    catch(err) {
        console.log("fail, success -> fail", console.error(err.message));
    }

    try {
        await checkSuccess(failedPromise(new Error("Hahaha I made you fail")), failedPromise(new Error("Hahaha I made you fail")));
        console.log("fail, fail -> success");
    }
    catch(err) {
        console.log("fail, fail -> fail", console.error(err.message));
    }

    try {
        await checkSuccess(successfulPromise(), successfulPromise());
        console.log("success, success -> success");
    }
    catch(err) {
        console.log("success, success -> fail", console.error(err.message));
    }
}

const usingThen_o = true;
if(usingThen_o) {
    usingThen();
}
else {
    usingAwait();
}