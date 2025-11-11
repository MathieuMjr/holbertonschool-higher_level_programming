#!/usr/bin/node

const arg = process.argv[2];
const number = parseInt(arg);
/* +var permet de transformer une string en nombre;
Number(...) aussi et conserve les chiffres après la virgule;
parsInt(...) converti en entier;
Si pas un chiffre passé en string, retourne NaN; */

if (!isNaN(number)) {
  console.log('My number: ' + number);
} else {
  console.log('Not a number');
}
