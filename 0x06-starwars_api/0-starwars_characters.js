#!/usr/bin/node
/**
 * Here we are trying to create an api script that will help us
 * to get all the characters of a star wars movie, cool right!!
 */

const request = require('request');

const movieEndpoint = 'https://swapi-api.alx-tools.com/api/films/' + definedMovieID;
const definedMovieID = process.argv[2];

function sendRequest (characterList, index) {
  if (characterList.length === index) {
    return;
  }

  request(characterList[index], (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      sendRequest(characterList, index + 1);
    }
  });
}

request(movieEndpoint, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const characterList = JSON.parse(body).characters;

    sendRequest(characterList, 0);
  }
});
