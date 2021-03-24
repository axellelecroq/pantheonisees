var input = document.querySelector('#inputStatus')
var selectedStatus = document.querySelector('#status')
selectedStatus.addEventListener('change', () => {
    switch (selectedStatus.value) {
        case 'lettres':
            input.setAttribute('value', 'lettre');
            break;
        case 'sciences':
            input.setAttribute('value', 'scientifique');
            break;
        case 'religion':
            input.setAttribute('value', 'religieux');
            break;
        case 'politique':
            input.setAttribute('value', 'politique');
            break;
        case 'loi':
            input.setAttribute('value', 'loi');
            break;
        case 'résistant':
            input.setAttribute('value', 'résistant');
            break;
        case 'militaire':
            input.setAttribute('value', 'militaire');
            break;
    }
})