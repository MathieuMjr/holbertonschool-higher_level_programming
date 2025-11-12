let charName = '';

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
    charName = data.name;
    const charElem = document.querySelector('#character');
    charElem.textContent = charName;
  });
