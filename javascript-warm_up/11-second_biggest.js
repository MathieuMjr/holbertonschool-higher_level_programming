#!/usr/bin/node

let biggest = 0;
let secondBiggest = 0;
let counter = 2;

while (process.argv[counter] !== undefined) {
  const current = parseInt(process.argv[counter]);
  if (biggest < current) {
    secondBiggest = biggest;
    biggest = current;
  } else if (secondBiggest < current) {
    secondBiggest = current;
  }
  counter++;
}
console.log(secondBiggest);
