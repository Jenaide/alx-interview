#!/usr/bin/node
const request = require('request');
const API = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  request(`${API}/films/${process.argv[2]}/`, (err, _, body) => {
    if (err) {
      console.error(err); // Log the error
      return;
    }
    const charURL = JSON.parse(body).characters;
    const charName = charURL.map(
      url => new Promise((resolve, reject) => {
        request(url, (promiseErr, __, charReqBody) => {
          if (promiseErr) {
            reject(promiseErr); // Reject the promise on error
            return; // Return to prevent resolving after rejection
          }
          resolve(JSON.parse(charReqBody).name);
        });
      }));

    Promise.all(charName)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.error(allErr)); // Log the error
  });
}
