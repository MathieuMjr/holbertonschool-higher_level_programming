const item = document.querySelector('#add_item');
const list = document.querySelector('.my_list');

function addToList () {
  const newItem = document.createElement('li');
  newItem.textContent = 'New Item wololo';
  list.appendChild(newItem);
}

item.addEventListener('click', addToList);
