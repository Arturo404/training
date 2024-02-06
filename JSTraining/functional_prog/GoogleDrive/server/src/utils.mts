export interface FileInfoInt {
    fileName: string;
    fileType: string;
    fileData: string;
};

export class FileInfo implements FileInfoInt {
    fileName: string;
    fileType: string;
    fileData: string;
    constructor(fileName: string, fileType: string, fileData:string) {
        this.fileName = fileName;
        this.fileType = fileType;
        this.fileData = fileData;
    }
};


export function fileInfoToFileName(fileInfo: FileInfo) {
    return `${fileInfo.fileName}.${fileInfo.fileType}`;
}

export function isJsonString(str:string) {
    try {
        JSON.parse(str);
    } catch (e) {
        return false;
    }
    return true;
}

export enum StatusResponse {
    FAILURE = 0,
    SUCCESS = 1
}

export interface FileCreationResponseInt {
    fileInfo: FileInfo;
    status: StatusResponse;
}

export class FileCreationResponse implements FileCreationResponseInt{
    fileInfo: FileInfo;
    status: StatusResponse;
    constructor(fileInfo: FileInfo, status: StatusResponse) {
        this.fileInfo = fileInfo;
        this.status = status;
    }
}