var inputGender = document.querySelector('#inputGender')
var selectedGender = document.querySelector('#gender')

selectedGender.addEventListener('change', () => {
    switch (selectedGender.value) {
        case 'femme':
            inputGender.setAttribute('value', 'femme');
            break;
        case 'homme':
            inputGender.setAttribute('value', 'homme');
            break;
        case 'autre':
            inputGender.setAttribute('value', 'autre');
            break;
    }
})