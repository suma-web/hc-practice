let allData = [];


function jsonList(list) {
    const ul = document.getElementById('list');
    ul.innerHTML = '';

    list.forEach(({ name, image }) => {
        const li = document.createElement('li');
        li.textContent = name;

        const img = document.createElement('img');
        img.src = `https://ihatov08.github.io${image}`;

        ul.appendChild(li);
        li.append(img);
    });
}

async function characterList() {
    const res = await fetch('https://ihatov08.github.io/kimetsu_api/api/all.json');
    allData = await res.json();

    jsonList(allData);

    document.querySelectorAll('input[name="btnradio"]').forEach(radio => {
        radio.addEventListener('change', () => {

            const value =  document.querySelector('input[name="btnradio"]:checked').value;
            if (value === 'all'){
                jsonList(allData);
            } else {
                const filtered = allData.filter(item => 
                    item.category === value
                );
                jsonList(filtered);
            }

        });
    })
};

characterList();