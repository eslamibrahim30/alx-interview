#!/usr/bin/node
const request = require('request');
const filmID = process.argv.slice(2)[0];
const url = 'https://swapi-api.alx-tools.com/api/films/';
request(url, function (error, response, body) {
  if (error) {
    throw error;
  }
  const chars = JSON.parse(body).results[parseInt(filmID) - 1].characters;
  for (let i = 0; i < chars.length; i++) {
    request(chars[i], function (error, response, body) {
      if (error) {
        throw error;
      }
      console.log(JSON.parse(body).name);
    });
  }
});

