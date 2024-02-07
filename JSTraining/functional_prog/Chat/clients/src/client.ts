import WebSocket from 'ws';
import {log4TSProvider} from "./logConfig.js";
import * as repl from 'repl';
import * as utils from './utils.mjs';
import chalk, { ChalkInstance } from 'chalk';

const port_socket = 8080;
const log = log4TSProvider.getLogger("client");

let local_client_id:number;

const client_socket: WebSocket = new WebSocket(`ws://localhost:${port_socket}`);

client_socket.on('open', () => {
    log.info("[Client] Connected to Chat.");
});

client_socket.on('message', (message: string) => {
    if(utils.isJsonString(message)) {
        const message_object: object = JSON.parse(message);
        if(message_object.hasOwnProperty("client_id")) {
            //Allocating client id to this client.
            local_client_id = (message_object as utils.IdAllocation).client_id;
            console.log(`You are Client ${local_client_id}`);
            
            const options = { useColors: true, prompt: '> ' };
            const repl_instance = repl.start(options);
            repl_instance.defineCommand('sendTo', {
                help: 'Send message to specific client',
                action(destAndContent:string) {
                    this.clearBufferedCommand();
                    const messageComponents: string[] = destAndContent.split(' ');
                    const client_id = Number(messageComponents[0]);
                    if(client_id == local_client_id) {
                        console.log(`You can't send message to yourself..`);
                        this.displayPrompt();
                        return;
                    }
                    const message = messageComponents.slice(1).join(' ');
                    const messageInfo: utils.MessageInfoInt = {
                        src: local_client_id,
                        dest:client_id,
                        message:message,
                        global:false,
                        color:undefined
                    }
                    client_socket.send(JSON.stringify(messageInfo));
                    this.displayPrompt();
                },
            });

            repl_instance.defineCommand('sendToAll', {
                help: 'Send message to all of the clients',
                action(message:string) {
                    this.clearBufferedCommand();
                    const messageInfo: utils.MessageInfoInt = {
                        src: local_client_id,
                        dest:-1,
                        message:message,
                        global:true,
                        color:undefined
                    }
                    client_socket.send(JSON.stringify(messageInfo));
                    this.displayPrompt();
                },
            });
        }
        else if(message_object.hasOwnProperty("message")) {
            //Receiving new message
            const messageInfo: utils.MessageInfoInt = (message_object as utils.MessageInfoInt);
            const src_color: utils.Color = messageInfo.color as utils.Color;
            console.log(utils.ColorToChalk(src_color)(`Client ${messageInfo.src}: ${messageInfo.message}`));
        }
    }
    else {
        console.log(`${message}`);
    }
});

client_socket.on('close', () => {
    log.info('Client disconnected');
});





