#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (_err, _response, body) => {
  const data = JSON.parse(body);
  console.log(data.title);
});
