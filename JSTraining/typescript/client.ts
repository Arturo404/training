import axios, { AxiosInstance } from 'axios';
import * as dotenv from "dotenv";
import { Credentials } from './credentials.js';
import Logger from 'js-logger';

dotenv.config();

const port: number = Number(process.env.PORT) || 3000;
const hostname: string = process.env.HOSTNAME || 'localhost';
const url_base: string = `http://${hostname}:${port}`;

const client: AxiosInstance = axios.create({
    baseURL: url_base
});

const signUp = async (username: string, password: string) : Promise<void> => {
    try {
        const {data} = await client.post('/signup', new Credentials(username, password));
        Logger.info(data);
    }
    catch(err: any) {
        Logger.error(`Client request error: ${err.message}`);
    }
}

