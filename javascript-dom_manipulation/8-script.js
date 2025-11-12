document.addEventListener('DOMContentLoaded', () => {
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => response.json())
    .then(data => {
      const helloElem = document.querySelector('#hello');
      helloElem.textContent = data.hello;
    });
});
