import fs from "fs";
import { filesData } from "./data.js";
import Logger from "js-logger";

const filesDirPath = "./created_files/";

Logger.useDefaults();

const createFile = async (fileName, fileType, fileData) => {
    const fullFilePath = `${filesDirPath}${fileName}.${fileType}`;
    try {
        await fs.writeFile(fullFilePath, fileData.toString(), (err) => {
            if (err) throw err;
        });
    }
    catch(err) {
        Logger.error(err.message)
    }
}

const treatFileEntry = async (value) => {
    const fileName = value.fileName;
    const fileType = value.fileType;
    const fileData = value.fileData;

    await createFile(fileName, fileType, fileData);
}


const fileCreator = async (filesData) => {
    for(const fileEntry of filesData) {
        await treatFileEntry(fileEntry);
    }
}



fileCreator(filesData);