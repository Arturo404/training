const array_num = [5,45,9,12,56,7,14];

function minByPromises(array_num) {
    let array_promises = array_num.map(async (num)=>{
        return new Promise((resolve)=>{
            setTimeout(()=>{
                resolve(num);
            }, num);
        });
    });

    return Promise.race(array_promises)
}

function usingThen(array_num) {
    console.log("Using then: ");
    minByPromises(array_num).then((result)=>{console.log(result);});
}

async function usingAwait(array_num) {
    console.log("Using await: ");
    try {
        console.log(await minByPromises(array_num));
    }
    catch(err) {
        console.log(err.message);
    }
}

const usingThen_o = false;
if(usingThen_o) {
    usingThen(array_num);
}
else {
    usingAwait(array_num);
}