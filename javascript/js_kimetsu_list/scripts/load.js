const character = document.getElementById('character');

export const loading = {
    show(){
        character.classList.add('hidden');
        document.getElementById('loading').classList.remove('hidden');
    },
    hide(){
        document.getElementById('loading').classList.add('hidden'); 
        character.classList.remove('hidden');
    } 
}