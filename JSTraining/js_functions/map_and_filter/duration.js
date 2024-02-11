array_durations = [3,45,2,345,22,11,76,43,24,56,7,2234];

const hoursToDays = (duration_hours) => {
    return duration_hours/24;
}

const SelectAndMapToDays = (array_durations) => {
    const array_mapped = array_durations.filter((duration)=>{return duration>24;}).map(hoursToDays);
    return array_mapped;
}

console.log(SelectAndMapToDays(array_durations));