#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) {
    console.error('Error: ', err);
  }

  console.log(data);
});
