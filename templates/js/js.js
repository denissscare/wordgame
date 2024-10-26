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
            if (data.valideWords === 403) printErrorMessage(data.letters);
        })
        .catch(err => console.error(err))
}

const addButtons = (letters) => {
    const buttons = document.getElementById("buttons");
    for(let i = 0; i < letters.lenght; i++){
        let div = document.createElement('div');
        div.className = 'button';
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