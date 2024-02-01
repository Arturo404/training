const array_num = [3,4,2,7,1,6];

function printNumber(num) {
    return ()=>{console.log(num);};
}

function numberPromiseIntervals(array_num) {
    let array_promises = array_num.map(async (num)=>{
        return new Promise((resolve)=>{
            const interval_id = setInterval(printNumber(num), 1.5*1000);
            setTimeout(()=>{
                clearInterval(interval_id);
                resolve();
            }, 30*1000);
        });
    });

    return Promise.all(array_promises);
}


function usingThen(array_num) {
    console.log("Using then: ");
    numberPromiseIntervals(array_num).then((results)=>{});
}

async function usingAwait(array_num) {
    console.log("Using await: ");
    try {
        await numberPromiseIntervals(array_num);
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