import express, { Request, Response } from 'express';
import { Credentials } from './credentials.mjs';
import bodyParser from 'body-parser';

let credentials: Credentials[]  = []

const app = express();
app.use(bodyParser.json());

const port: number = Number(process.env.PORT) || 3000;
const hostName: string = `localhost`;

app.post('/signup', (req: Request, res: Response) => {
    console.log("received request");
    const userCredentials: Credentials = req.body;
    for(const credential of credentials) {
        if(credential.username == userCredentials.username) {
            if(credential.password == userCredentials.password) {
                console.log("Existing credentials: given credentials are correct.");
                res.send("Existing credentials: given credentials are correct.");
                return;
            }
            else {
                console.log("Existing credentials: given credentials are incorrect.");
                res.send("Existing credentials: given credentials are incorrect.");
                return;
            }
        }
    }

    credentials.push(new Credentials(userCredentials.username, userCredentials.password));
    console.log("Non-existing credentials: new credentials have been registered.");
    res.send("Non-existing credentials: new credentials have been registered.");
    return;
});

try {
    app.listen(port,  hostName, () => {
        console.log(`Server running at ${hostName}:${port}`);
    });
}
catch(err: any) {
    console.log(`Error initializing server: ${err.message}`)
}
