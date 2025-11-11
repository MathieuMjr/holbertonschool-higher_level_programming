#!/usr/bin/node

const size = parseInt(process.argv[2]);
let counter1 = 0;
let counter2 = 0;
let string = '';

if (isNaN(size) || size === undefined) {
  console.log('Missing size');
} else {
  while (counter1 < size) {
    string += 'X';
    counter1++;
  }
  while (counter2 < size) {
    console.log(string);
    counter2++;
  }
}
