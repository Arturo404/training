import WebSocket, { WebSocketServer } from 'ws';
import {log4TSProvider} from "./logConfig.js";
import * as Utils from './utils.mjs';
import * as fs from 'fs';

const server_dir_path:string = "C:/Users/Arthur/Desktop/INFORMATIQUE/training/JSTraining/functional_prog/GoogleDrive/";

const log = log4TSProvider.getLogger("server");

const port = 8080;

const server_socket: WebSocketServer= new WebSocketServer({port});

server_socket.on('connection', (client_socket: WebSocket) => {
    log.info('New client connected');

    client_socket.on('message', (message: string) => {
        if(Utils.isJsonString(message)) {
            log.info(`Received request to create new file: ${message}`);
            const fileInfoToCreate: Utils.FileInfoInt = JSON.parse(message);
            const fileName: string = Utils.fileInfoToFileName(fileInfoToCreate);
            const filePath: string = `${server_dir_path}${fileName}`;

            fs.writeFileSync(filePath, fileInfoToCreate.fileData, 'utf-8');
            log.info(`New file created.`);
            const fileCreationResponse: Utils.FileCreationResponse = new Utils.FileCreationResponse(fileInfoToCreate, Utils.StatusResponse.SUCCESS);
            client_socket.send(JSON.stringify(fileCreationResponse));
        }
        else {
            log.info(`Message is out of protocol: ${message}`);
        }

    });

    client_socket.on('close', () => {
        log.info('Client disconnected');
    });

});

log.info(`[Server] Listening on port: ${port}`);