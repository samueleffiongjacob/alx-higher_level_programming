#!/usr/bin/node

/**
 * old one
 * const fs = require('fs');
 * const fileA = fs.readFileSync(process.argv[2], 'utf8');
 * const fileB = fs.readFileSync(process.argv[3], 'utf8');
 * fs.writeFileSync([4], fileA + fileB);
process.argv
 */

const fs = require('fs');
const path = require('path');

// Ensure proper usage
if (process.argv.length !== 5) {
    console.log('Usage: node concatFiles.js <file1> <file2> <destination>');
    process.exit(1);
}

// Extract file paths from command line arguments
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

// Concatenate files asynchronously
fs.readFile(fileA, 'utf8', (err, data1) => {
    if (err) {
        console.error(`Error reading ${fileA}: ${err}`);
        return;
    }

    fs.readFile(fileB, 'utf8', (err, data2) => {
        if (err) {
            console.error(`Error reading ${fileB}: ${err}`);
            return;
        }

        const concatenatedData = `${data1.trim()}\n${data2.trim()}\n`;

        // Write concatenated data to destination file
        fs.writeFile(fileC, concatenatedData, (err) => {
            if (err) {
                console.error(`Error writing to ${fileC}: ${err}`);
                return;
            }
            console.log(`Concatenated files saved to ${fileC}`);
        });
    });
});
