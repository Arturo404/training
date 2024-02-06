import chalk, { ChalkInstance } from 'chalk';

export interface MessageInfoInt {
    src:number;
    dest:number;
    message:string;
    global:boolean;
    color:Color|undefined;
};

export interface IdAllocation {
    client_id:number;
};

export function isJsonString(str:string) {
    try {
        JSON.parse(str);
    } catch (e) {
        return false;
    }
    return true;
}

export interface ClientColor {
    client_id:number;
    color:Color;
};

export enum Color {
    BLUE = 0,
    GREEN,
    RED,
    YELLOW
}

export function ColorToChalk(color:Color) : ChalkInstance {
    switch(color) {
        case Color.BLUE:
            return chalk.blue;
        case Color.GREEN:
            return chalk.green;
        case Color.RED:
            return chalk.red;
        case Color.YELLOW:
            return chalk.yellow;
    }
}