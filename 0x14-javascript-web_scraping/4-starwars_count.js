#!/usr/bin/node

const request = require('request');

// The URL of the Star Wars API for films
const url = process.argv[2];

// The character ID for Wedge Antilles
const characterId = 18;
const characterUrl = `https://swapi-api.alx-tools.com/api/people/${characterId}/`;

request(url, (_err, _response, body) => {
  const data = JSON.parse(body).results;
  let count = 0;

  data.forEach(film => {
    if (film.characters.includes(characterUrl)) {
      count++;
    }
  });

  console.log(count);
});
