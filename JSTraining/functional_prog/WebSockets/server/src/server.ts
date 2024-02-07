import WebSocket, { WebSocketServer } from 'ws';
import {log4TSProvider} from "./logConfig.js";

const log = log4TSProvider.getLogger("server");

const port = 8080;

const server_socket: WebSocketServer= new WebSocketServer({port});

let guess: {guess:number} = {guess: 0};

server_socket.on('connection', (client_socket: WebSocket) => {
    log.info('New client connected');

    client_socket.on('message', (message: string) => {
        if(message == "Start guessing!" || message == "Try again") {
            if(guess.guess > 100) {
                client_socket.close();
                return;
            }
            log.info(() => `Guessing ${guess.guess}`);
            client_socket.send(JSON.stringify(guess));
            guess.guess += 1;
        }
        else if(message == "Success") {
            log.info("I won! Game finished.");
            return;
        }
        else {
            log.info(() => `Message is out of protocol, message received: ${message}`);
        }
    });

    client_socket.on('close', () => {
        log.info('Client disconnected');
    });
});