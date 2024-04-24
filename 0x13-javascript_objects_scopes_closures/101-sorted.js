#!/usr/bin/node

// Importing the dictionary from 101-data.js
const { dict } = require('./Helper/101-data');

const output = {};

for (const entry in dict) {
  if (!output[dict[entry]]) output[dict[entry]] = [];
  output[dict[entry]].push(entry);
}

console.log(output);


// Computing the new dictionary
const newDict = output;

// Printing the new dictionary
console.log(newDict);


