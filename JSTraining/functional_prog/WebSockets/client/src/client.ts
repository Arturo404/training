import WebSocket from 'ws';
import {log4TSProvider} from "./logConfig.js";
import { getRandomInt, isJsonString } from "./utils.js";

const port = 8080;
const log = log4TSProvider.getLogger("client");

let numberToGuess: number;

const client_socket: WebSocket = new WebSocket(`ws://localhost:${port}`);

client_socket.on('open', () => {
    log.info("[Client] Connect to server.");
    numberToGuess = getRandomInt(1,100);

    log.info("[Client] Chose number to guess.");
    //send to server that number chosen
    client_socket.send("Start guessing!");
});

client_socket.on('message', (message: string) => {
    if(message == "Calculating next guess..") return;
    else if(isJsonString(message)) {
        const current_guess: {guess:number} = JSON.parse(message);
        if(current_guess.guess == numberToGuess) {
            client_socket.send("Success");
            client_socket.close();
        }
        else {
            client_socket.send("Try again");
        }
    }
    else {
        log.info(() => `Message is out of protocol, message received: ${message}`);
    }
});

client_socket.on('close', () => {
    log.info('Client disconnected');
});







