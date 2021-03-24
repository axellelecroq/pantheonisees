var input = document.querySelector('#inputGender')
var selectedGender = document.querySelector('#gender')

selectedGender.addEventListener('change', () => {
    switch (selectedGender.value) {
        case 'femme':
            input.setAttribute('value', 'femme');
            break;
        case 'homme':
            input.setAttribute('value', 'homme');
            break;
        case 'autre':
            input.setAttribute('value', 'autre');
            break;
    }
})