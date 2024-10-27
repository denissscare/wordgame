window.onload = () => {
    const input = document.getElementById('enterWord')
    input.addEventListener('keyup', event => {
        if(event.key == 'Enter'){
            getWordFromBack(input.value);
        }
    });
}

const getWordFromBack = word => {
    fetch(`http://127.0.0.1:8000/getWord/${word}`)
        .then(resp => resp.json())
        .then(data => {
            console.log(data);
            if (data.hasOwnProperty('detail')) {
                printErrorMessage(data.detail);
            }
            addButtons(data.letters)
        })
        .catch(err => console.error('Ошибка: ' + err))
}

const addButtons = (letters) => {
    const buttons = document.getElementById("buttons");
    console.log(letters.length);
    for(let i = 0; i < letters.length; i++){
        let div = document.createElement('div');
        div.className = 'button';
        const h = document.createElement('H1');
        h.className = 'letter';
        h.innerHTML = letters[i].toUpperCase();
        div.appendChild(h);
        buttons.append(div);
    }
}

const printErrorMessage = (message) => {
    const buttons = document.getElementById("buttons");
    buttons.innerHTML = '';
    const h = document.createElement('H1');
    h.className = 'error-message';
    h.innerHTML = message;
    buttons.appendChild(h);
} 