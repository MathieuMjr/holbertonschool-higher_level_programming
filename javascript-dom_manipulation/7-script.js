const titleList = [];

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    data.results.forEach(film => {
      titleList.push(film.title);
    });
    const movieElem = document.querySelector('#list_movies');
    titleList.forEach(title => {
      const newItem = document.createElement('li');
      newItem.textContent = title;
      movieElem.appendChild(newItem);
    });
  });
