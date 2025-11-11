const header = document.querySelector('header');
const redHeader = document.querySelector('#red_header');

function addRed () {
  header.classList.add('red');
} /*ajoute le style sans écraser les autres styles*/

redHeader.addEventListener('click', addRed);
