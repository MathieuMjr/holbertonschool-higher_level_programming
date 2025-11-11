#!/usr/bin/node

let counter = 2;
let biggest = 0;

while (process.argv[counter] !== undefined) {
  if (biggest < parseInt(process.argv[counter])) {
    biggest = parseInt(process.argv[counter]);
  }
  counter++;
}
if (counter > 3) {
  console.log(biggest);
} else {
  console.log(0);
}
