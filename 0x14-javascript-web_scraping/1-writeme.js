#!/usr/bin/node
const fs = require('fs');

function writeFile (filePath, content) {
  fs.writeFile(filePath, content, 'utf8', (err) => {
    if (err) {
      console.error(err);
    }
  });
}

if (process.argv.length === 4) {
  const filePath = process.argv[2];
  const content = process.argv[3];
  writeFile(filePath, content);
}
