import axios from 'axios';
import * as dotenv from "dotenv";
import { Credentials } from './credentials.mjs';

dotenv.config();

const port = process.env.PORT || 3000;
const url_base = `http://localhost:${port}`;

const client = axios.create({
    baseURL: url_base
});

const signUp = async (username: string, password: string) => {
    try {
        const {data} = await client.post('/signup', new Credentials(username, password));
        console.log(data);
    }
    catch(err: any) {
        console.error(`Client request error: ${err.message}`);
    }
}

