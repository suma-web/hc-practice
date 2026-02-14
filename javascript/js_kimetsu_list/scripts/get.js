import { loading } from "./load.js";


const BASE_URL = 'https://ihatov08.github.io'

function jsonList(list) {
    const ul = document.getElementById('list');
    ul.innerHTML = '';

    list.forEach(({ name, image }) => {
        const li = document.createElement('li');
        li.textContent = name;

        const img = document.createElement('img');
        img.src = BASE_URL + image;

        ul.appendChild(li);
        li.append(img);
    });
}

async function updateView() {
    loading.show();
    await new Promise(resolve => setTimeout(resolve, 1500));

    const value =
      document.querySelector('input[name="btnradio"]:checked').value;

    const res = await fetch('https://ihatov08.github.io/kimetsu_api/api/all.json');
    const data = await res.json();

    if (value === 'all') {
        jsonList(data);
    } else {
        jsonList(data.filter(item => item.category === value));
    }
    
    loading.hide();
}

document.querySelectorAll('input[name="btnradio"]')
  .forEach(radio => {
        radio.addEventListener('change', updateView);
  });

updateView();