#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const characterId = '18';

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const films = JSON.parse(body).results;
  const wedgeMovies = films.filter((film) =>
    film.characters.some((character) => character.endsWith(characterId))
  );
  console.log(`${wedgeMovies.length}`);
});
