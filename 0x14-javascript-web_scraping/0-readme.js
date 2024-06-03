#!/usr/bin/node
const fs = require('fs');

process.argv[0] = 'node';
function readFile (filePath) {
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(data);
  });
}

if (process.argv.length === 3) {
  const filePath = process.argv[2];
  readFile(filePath);
}
