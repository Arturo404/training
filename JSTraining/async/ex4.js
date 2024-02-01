const array_num = [2,5,45,2,12,56,7,2];

let array_sorted = [];

function sortArrayPromise(array_num) {
    const max_array = Math.max(...array_num);
    let array_promises = array_num.map(async (num)=>{
        return new Promise((resolve)=>{
            setTimeout(()=>{
                array_sorted.push(num);
                resolve();
            }, max_array-num);
        });
    });

    return Promise.all(array_promises);
}

function sortArrayUsingThen(array_num) {
    sortArrayPromise(array_num).then((results)=>{console.log("Using then: ", array_sorted);});
}

async function sortArrayUsingAwait(array_num) {
    await sortArrayPromise(array_num);
    console.log("Using await: ", array_sorted);
}

const usingThen = false;
if(usingThen) {
    sortArrayUsingThen(array_num);

}
else {
    sortArrayUsingAwait(array_num);
}
