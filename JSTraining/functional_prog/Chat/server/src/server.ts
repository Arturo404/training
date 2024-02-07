import WebSocket, { WebSocketServer } from 'ws';
import {log4TSProvider} from "./logConfig.js";
import * as utils from './utils.mjs';
import chalk, { ChalkInstance } from 'chalk';

let colors: utils.Color[] = [utils.Color.BLUE, utils.Color.GREEN, utils.Color.RED, utils.Color.YELLOW];
let clients_colors: utils.ClientColor[] = [];

const log = log4TSProvider.getLogger("server");

const port = 8080;
const server_socket: WebSocketServer= new WebSocketServer({port});

server_socket.on('connection', (client_socket: WebSocket) => {
    const client_id:number = server_socket.clients.size;
    log.info(`New client connected- id: ${client_id}`);
    const allocationInfo: utils.IdAllocation = {client_id:client_id};
    client_socket.send(JSON.stringify(allocationInfo));


    client_socket.on('message', (message: string) => {
        if(utils.isJsonString(message)) {
            const message_object: object = JSON.parse(message);
            if(message_object.hasOwnProperty("message")) {
                const messageInfo: utils.MessageInfoInt = (message_object as utils.MessageInfoInt);
                let src_color:utils.Color|undefined = undefined;
                for(const client of clients_colors) {
                    if(client.client_id == messageInfo.src) {
                        src_color = client.color;
                    }
                }
                if(!src_color) {
                    src_color = colors.pop();
                    clients_colors.push({client_id:messageInfo.src, color:(src_color as utils.Color)})
                }
                src_color = src_color as utils.Color;
                messageInfo.color = src_color;
                if(messageInfo.global) {
                    let index:number = 1;
                    for(const currClient of server_socket.clients) {
                        if(index != messageInfo.src) {
                            currClient.send(JSON.stringify(messageInfo));
                        }
                        index+=1;
                    }
                }
                else {
                    let index:number = 1;
                    for(const currClient of server_socket.clients) {
                        if(index == messageInfo.dest) {
                            currClient.send(JSON.stringify(messageInfo))
                            return;
                        }
                        index+=1;
                    }
                    log.info(`Client ${messageInfo.src} tried to talk with client ${messageInfo.dest} that doesn't exist.`);
                    client_socket.send(`You tried to talk with client ${messageInfo.dest} that doesn't exist.`)
                }
            }
            else {
                log.info(`Message out of protocol: ${message}`);
            }
        }
    });

    client_socket.on('close', () => {
        log.info('Client disconnected');
    });

});

log.info(`[Server] Listening on port: ${port}`);