import express, { Request, Response } from 'express';
import * as Utils from './utils.mjs';
import bodyParser from 'body-parser';
import WebSocket from 'ws';
import {log4TSProvider} from "./logConfig.js";
import * as fs from 'fs';


const server_dir_path:string = "C:/Users/Arthur/Desktop/INFORMATIQUE/training/JSTraining/functional_prog/GoogleDrive/";

const port_app_client: number = 3000;
const hostName_client: string = `localhost`;


const port_socket = 8080;
const log = log4TSProvider.getLogger("client");


const app_client = express();
app_client.use(bodyParser.json());

app_client.post('/upload_file', (req: Request, res: Response) => {
    log.info("Received new request to upload file to server.");
    const fileInfo: Utils.FileInfoInt = req.body;
    const fileInfo_str: string = JSON.stringify(fileInfo);

    const client_socket: WebSocket = new WebSocket(`ws://localhost:${port_socket}`);

    client_socket.on('open', () => {
        log.info("[Client] Connected to server.");
        client_socket.send(fileInfo_str);
        log.info(`New file sent to server: ${fileInfo_str}`);
    });

    client_socket.on('message', (message: string) => {

            if(Utils.isJsonString(message)) {
                const message_object: Utils.FileCreationResponseInt = JSON.parse(message);
                const curr_fileInfo: Utils.FileInfo = message_object.fileInfo;

                const fileName: string = Utils.fileInfoToFileName(curr_fileInfo);
                const filePath: string = `${server_dir_path}${fileName}`;

                const fileContent:string = fs.readFileSync(filePath, 'utf-8');
                log.info(`Checking file ${filePath}, \ncontent expected: "${curr_fileInfo.fileData}", \ncontent found: "${fileContent}"`);

                if(fileContent == curr_fileInfo.fileData) {
                    log.info(`Identical content! Success`);
                }
                else {
                    log.info(`Differences found.. Failure`);
                }
            }
            else {
                log.info(`Message out of protocol: ${message}`);
            }
            client_socket.close();
    });

    client_socket.on('close', () => {
        log.info('Client disconnected');
    });

    res.status(200).send("Received request, transmitting to server.");
    return;
});

try {
    app_client.listen(port_app_client,  hostName_client, () => {
        console.log(`Client app running at ${hostName_client}:${port_app_client}`);
    });
}
catch(err: any) {
    console.log(`Error initializing client app: ${err.message}`)
}







