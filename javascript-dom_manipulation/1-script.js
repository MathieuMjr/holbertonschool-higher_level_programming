const header = document.querySelector('header');
const redHeader = document.querySelector('#red_header');

function toRed () {
  header.style.color = '#FF0000';
}

redHeader.addEventListener('click', toRed);
