const header = document.querySelector('header');
const update = document.querySelector('#update_header');

function updateHeader () {
  header.textContent = 'New Header!!!';
}

update.addEventListener('click', updateHeader);
