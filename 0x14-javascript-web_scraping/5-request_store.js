#!/usr/bin/node

const fs = require('fs');
const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err) {
    console.error(err);
  } else if (response.statusCode === 200) {
    fs.writeFile(process.argv[3], body, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  } else {
    console.error(response.statusCode);
  }
});
