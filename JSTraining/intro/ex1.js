const fs = require("fs");

const filesDirPath = "./created_files/"

const filesData = [
    {
        fileName: "number",
        fileType: "txt",
        fileData: 122
    },
    {
        fileName: "func",
        fileType: "js",
        fileData: "console.log('Hello World!');"
    },
    {
        fileName: "myname",
        fileType: "txt",
        fileData: "PSI Course"
    },
    {
        fileName: "veryLongString",
        fileType: "txt",
        fileData: "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    }
];

function createFile(fileName, fileType, fileData) {
    const fullFilePath = `${filesDirPath}${fileName}.${fileType}`;
    try {
        fs.writeFile(fullFilePath, fileData.toString(), (err) => {
            if (err) throw err;
        });
    }
    catch(err) {
        console.log(err.message)
    }
}

function treatFileObject(value) {
    const fileName = value.fileName;
    const fileType = value.fileType;
    const fileData = value.fileData;

    createFile(fileName, fileType, fileData);
}


function fileCreator(filesData) {
    filesData.forEach(treatFileObject); 
}



fileCreator(filesData);