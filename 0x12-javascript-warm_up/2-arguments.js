#!/usr/bin/node

const len = process.argv.length;

if (len ===  2) {
  console.log('Argument' + (len ===  3 ? 's' : ' ') + 'found');
} else  {
  console.log('No argument ');
}
