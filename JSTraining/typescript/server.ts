import express, { Request, Response } from 'express';
import { Credentials } from './credentials.js';
import bodyParser from 'body-parser';
import Logger from 'js-logger';

const credentials: Credentials[]  = [];

const app = express();
app.use(bodyParser.json());

const port: number = Number(process.env.PORT) || 3000;
const hostName: string = process.env.HOSTNAME || `localhost`;

app.post('/signup', (req: Request, res: Response) => {
    Logger.debug("received request");
    const userCredentials: Credentials = req.body;
    for(const credential of credentials) {
        if(credential.username === userCredentials.username) {
            if(credential.password === userCredentials.password) {
                res.send("Username found: given credentials are correct.");
                return;
            }
            else {
                res.send("Username found: incorrect password.");
                return;
            }
        }
        else {

        }
    }

    const newCredentials = new Credentials(userCredentials.username, userCredentials.password);
    credentials.push(newCredentials);
    res.send("Username not found: new credentials have been registered.");
    return;
});

try {
    app.listen(port,  hostName, () => {
        Logger.info(`Server running at ${hostName}:${port}`);
    });
}
catch(err: any) {
    Logger.error(`Error initializing server: ${err.message}`)
}
