#!/usr/bin/node

const list = require('./Helper/100-data').list;

const new_list = list

const map = list.map((x, i) => x * i)

console.log( new_list);
console.log(map);
