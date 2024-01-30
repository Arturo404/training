const readline = require('readline');
const fs = require('fs');



const caseFilesDirPath = "./case_files/"
const streetNamesFileName = "street_names.txt"

const streetNamesFilePath = caseFilesDirPath+streetNamesFileName

function firstLetterToUpperCase(string) {
    return string.charAt(0).toUpperCase()+string.slice(1).toLowerCase();
}


try {
    fs.readdir(caseFilesDirPath, function (err, files) {
        if (err) {
          console.error("Could not list the directory.", err);
          process.exit(1);
        }
    
        files.forEach(function (file) {
            if(file.includes("Case")) {
                fs.unlink(`${caseFilesDirPath}${file}`, (err) => {
                    if (err) throw err;
                }); 
            }
        });
    
    });
}
catch(err) {
    console.log(`Error erasing case files: ${err.message}`)
}

try {
    const rl = readline.createInterface({
        input: fs.createReadStream(streetNamesFilePath)
    });

    rl.on('line', (line) => {

        if(!line.includes("|")) return;
        const lineComponents = line.split("|");
        const caseName = lineComponents[0], streetName = lineComponents[1];
        
        const streetNameComponents = streetName.split(" ");
        let caseCorrectName = "";
    
        switch(caseName) {
            case "camelCase":
                for(let i=0; i<streetNameComponents.length; i++) {
                    if(i==0) {
                        caseCorrectName += streetNameComponents[i].toLowerCase();
                    }
                    else {
                        caseCorrectName += firstLetterToUpperCase(streetNameComponents[i]);
                    }
                }
                break;
            case "pascalCase":
                for(let i=0; i<streetNameComponents.length; i++) {
                    caseCorrectName += firstLetterToUpperCase(streetNameComponents[i]);
                }
                break;
            case "kebabCase":
                for(let i=0; i<streetNameComponents.length; i++) {
                    if(i==0) {
                        caseCorrectName += streetNameComponents[i].toLowerCase();
                    }
                    else {
                        caseCorrectName += "-"+streetNameComponents[i].toLowerCase();
                    }
                }
                
                break;
            case "snakeCase":
                for(let i=0; i<streetNameComponents.length; i++) {
                    if(i==0) {
                        caseCorrectName += streetNameComponents[i].toLowerCase();
                    }
                    else {
                        caseCorrectName += "_"+streetNameComponents[i].toLowerCase();
                    }
                }
                break;
            case "constantCase":
                for(let i=0; i<streetNameComponents.length; i++) {
                    if(i==0) {
                        caseCorrectName += streetNameComponents[i].toUpperCase();
                    }
                    else {
                        caseCorrectName += "_"+streetNameComponents[i].toUpperCase();
                    }
                }
                break;
            case "pathCase":
                for(let i=0; i<streetNameComponents.length; i++) {
                    if(i==0) {
                        caseCorrectName += firstLetterToUpperCase(streetNameComponents[i])
                    }
                    else {
                        caseCorrectName += "/"+streetNameComponents[i].toLowerCase();
                    }
                }
                break;
            default:
        } 
    
        const caseFilePath = `${caseFilesDirPath}${caseName}.txt`
        fs.appendFile(caseFilePath, caseCorrectName+"\n", 'utf8', function(err) {
            if (err) throw err;
        });
    });
    
}
catch(err) {
    console.log(err.message);
}



