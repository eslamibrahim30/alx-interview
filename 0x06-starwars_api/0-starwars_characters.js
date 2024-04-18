#!/usr/bin/node
const request = require('request');
const filmID = process.argv.slice(2)[0];
const url = 'https://swapi-api.alx-tools.com/api/films/';
function requestInfo (url) {
  return new Promise(function (resolve, reject) {
    request(url, function (error, res, body) {
      if (!error && res.statusCode === 200) {
        resolve(body);
      } else {
        reject(error);
      }
    });
  });
}

async function main () {
  const films = await requestInfo(url);
  const chars = JSON.parse(films).results[parseInt(filmID) - 1].characters;
  for (let i = 0; i < chars.length; i++) {
    const charName = await requestInfo(chars[i]);
    console.log(JSON.parse(charName).name);
  }
}

main();
