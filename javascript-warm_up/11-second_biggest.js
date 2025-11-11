#!/usr/bin/node
let array = []
let counter = 2;
let biggest = 0;
let counter2 = 0;
let scdbiggest = 0;

while (process.argv[counter] !== undefined) {
  array.push(parseInt(process.argv[counter]));
  if (biggest < parseInt(process.argv[counter])) {
    biggest = parseInt(process.argv[counter]);
  }
  counter++;
}

while (counter2 !== counter - 2) {
    if (scdbigget)
}
if (counter > 3) {
  console.log(biggest);
} else {
  console.log(0);
}
