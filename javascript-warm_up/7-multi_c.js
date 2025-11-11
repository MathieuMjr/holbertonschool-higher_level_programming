#!/usr/bin/node

const myString = 'C is fun';
const loop = process.argv[2];
let counter = 0;

if (loop === undefined) {
  console.log('Missing number of occurences');
} else {
  for (counter; counter < loop; counter++) {
    console.log(myString);
  }
}
