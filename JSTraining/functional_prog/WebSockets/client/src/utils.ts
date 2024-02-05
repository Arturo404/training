export function getRandomInt(min: number, max: number) {
    return Math.floor(Math.random() * (max - min) ) + min;
}

export function isJsonString(str:string) {
    try {
        JSON.parse(str);
    } catch (e) {
        return false;
    }
    return true;
}