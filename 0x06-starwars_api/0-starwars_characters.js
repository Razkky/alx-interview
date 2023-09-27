// Use star wars api to fetch list of characters in a movie
const request = require('request');

const movieId = process.argv[2];

const URL_ENDPOINT = 'https://swapi-api.alx-tools.com/api/';
const MOVIE_ENDPOINT = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request(MOVIE_ENDPOINT, (err, res, body) => {
  if (!err) {
    const movieName = JSON.parse(body).title;
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      try {
	fetchName(character)
	  .then(name => {
	    console.log(name);
	  })
      } catch (error) {
	console.log(error);
      }
    }
  } else {
    console.log('Error ' + err);
  }
})

function fetchName(url) {
  console.log('fettching ', url)
  return new Promise((resolve, reject) => {
    request(url, (err, res, body) => {
      if (!err) {
	const name = JSON.parse(body).name;
	resolve(name);
      } else {
	reject(err);
      }
    })
  })
}
// console.log(characterList);
// const characterList = [];
// async function getCharactersName () {
//   request(MOVIE_ENDPOINT, (err, res, body) => {
//     if (!err) {
//       const movieName = JSON.parse(body).title;
//       console.log(movieName);
//       const characters = JSON.parse(body).characters;
//       characters.forEach((character) => {
// 	request(character, (err, res, body) => {
// 	  if (!err) {
// 	    const characterName = JSON.parse(body).name;
// 	    console.log(characterName);
// 	  }
// 	})
//       })
//     } else {
//       console.log('Error ', err);
//     }
//   })
// }

// getCharactersName()

