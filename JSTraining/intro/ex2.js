import * as readline from 'readline';
import * as fs from 'fs';
import Logger from 'js-logger';

const caseFilesDirPath = "./case_files/"
const streetNamesFileName = "street_names.txt"

const streetNamesFilePath = caseFilesDirPath+streetNamesFileName

const firstLetterToUpperCase = (string) => {
    return string.charAt(0).toUpperCase()+string.slice(1).toLowerCase();
}

function deleteAllCaseFiles(caseFilesDirPath) {
    try {
        fs.readdir(caseFilesDirPath, function (err, files) {
            if (err) {
              Logger.error("Could not list the directory.");
              throw err;
            }
        
            files.forEach(function (file) {
                if(file.includes("Case")) {
                    fs.unlink(`${caseFilesDirPath}${file}`, (err) => {
                        if (err) {
                            Logger.error(`Could not delete file ${file}`);
                            throw err;
                        }
                    }); 
                }
            });
        
        });
    }
    catch(err) {
        Logger.error(`Error erasing case files`);
        throw err;
    }
}

function toCamelCase(words) {
    let caseResult = '';
    for(let i=0; i<words.length; i++) {
        if(i==0) {
            caseResult += words[i].toLowerCase();
        }
        else {
            caseResult += firstLetterToUpperCase(words[i]);
        }
    }
    return caseResult;
}

function toPascalCase(words) {
    let caseResult = '';
    for(let i=0; i<words.length; i++) {
        caseResult += firstLetterToUpperCase(words[i]);
    }
    return caseResult;
}

function toKebabCase(words) {
    let caseResult = '';
    for(let i=0; i<words.length; i++) {
        if(i==0) {
            caseResult += words[i].toLowerCase();
        }
        else {
            caseResult += "-"+words[i].toLowerCase();
        }
    }
    return caseResult;
}

function toSnakeCase(words) {
    let caseResult = '';
    for(let i=0; i<words.length; i++) {
        if(i==0) {
            caseResult += words[i].toLowerCase();
        }
        else {
            caseResult += "_"+words[i].toLowerCase();
        }
    }
    return caseResult;
}

function toConstantCase(words) {
    let caseResult = '';
    for(let i=0; i<words.length; i++) {
        if(i==0) {
            caseResult += words[i].toUpperCase();
        }
        else {
            caseResult += "_"+words[i].toUpperCase();
        }
    }
    return caseResult;
}

function toPathCase(words) {
    let caseResult = '';
    for(let i=0; i<words.length; i++) {
        if(i==0) {
            caseResult += firstLetterToUpperCase(words[i])
        }
        else {
            caseResult += "/"+words[i].toLowerCase();
        }
    }
    return caseResult;
}

function toDefault(words) {
    return '';
}

const caseFunctions = {
    'camelCase':toCamelCase,
    'pascalCase':toPascalCase,
    'kebabCase':toKebabCase,
    'snakeCase':toSnakeCase,
    'constantCase':toConstantCase,
    'pathCase':toPathCase,
    'default':toDefault
};

async function caseToFiles(streetNamesFilePath, caseFilesDirPath) {
    try {
        deleteAllCaseFiles(caseFilesDirPath);

        const rl = readline.createInterface({
            input: fs.createReadStream(streetNamesFilePath)
        });
    
        rl.on('line', (line) => {
            if(!line.includes("|")) return;
            const lineComponents = line.split("|", 2);
            const caseName = lineComponents[0], streetName = lineComponents[1];
            
            const streetNameComponents = streetName.split(" ");
            const caseFunctionToApply = caseFunctions[caseName] || caseFunctions['default'];
    
            const caseFilePath = `${caseFilesDirPath}${caseName}.txt`
            fs.appendFile(caseFilePath, caseFunctionToApply(streetNameComponents)+"\n", 'utf8', function(err) {
                if (err) throw err;
            });
        });

        await events.once(rl, 'close');
        
    }
    catch(err) {
        Logger.error(err.message);
    }
}


caseToFiles(streetNamesFilePath, caseFilesDirPath);

