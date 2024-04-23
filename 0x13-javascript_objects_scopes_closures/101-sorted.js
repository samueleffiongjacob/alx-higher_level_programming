#!/usr/bin/node

// Importing the dictionary from 101-data.js
const { dict } = require('./Helper/101-data');

// Function to compute the new dictionary
function computeDictionary(dict) {
    const result = {};

    // Iterate over each user id and its occurrence
    for (const userId in dict) {
        const occurrence = dict[userId];

        // If the occurrence doesn't exist as a key in result, create it with an empty array
        if (!result[occurrence]) {
            result[occurrence] = [];
        }

        // Push the user id to the array corresponding to its occurrence
        result[occurrence].push(parseInt(userId));
    }

    return result;
}

// Computing the new dictionary
const newDict = computeDictionary(dict);

// Printing the new dictionary
console.log(newDict);

/**
 * old way pure loop 
 
 * const { dict } = require('./Helper/101-data').dict;
  const output = {};

  for (const entry in dict) {
  if (!output[dict[entry]]) output[dict[entry]] = [];
  output[dict[entry]].push(entry);
  }

  console.log(output);
 */
