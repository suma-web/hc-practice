import { loading } from "./load.js";


const BASE_URL = 'https://ihatov08.github.io'

const categoryMap = {
  all: 'all.json',
  鬼殺隊: 'kisatsutai.json',
  柱: 'hashira.json',
  鬼: 'oni.json'
};


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

    const categoryName = categoryMap[value];

    const url = `https://ihatov08.github.io/kimetsu_api/api/${categoryName}`;

    try {
        const res = await fetch(url);
        if (!res.ok) throw new Error('API error');
        const data = await res.json();
        jsonList(data);
    } catch (err) {
        console.error(err);
    } finally {
        loading.hide();
    }
}

document.querySelectorAll('input[name="btnradio"]')
  .forEach(radio => {
        radio.addEventListener('change', updateView);
  });

updateView();