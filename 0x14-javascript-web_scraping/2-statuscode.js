#!/usr/bin/node

const request = require('request');

request(process.argv[2], (_err, response) => {
  console.log('code:', response.statusCode);
});
