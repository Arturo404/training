export const getRandomInt = (min: number, max: number) => {
    return Math.floor(Math.random() * (max - min) ) + min;
}

export const isJsonString = (str:string) => {
    try {
        JSON.parse(str);
    } catch (e) {
        return false;
    }
    return true;
}