var inputStatus = document.querySelector('#inputStatus')
var selectedStatus = document.querySelector('#status')

selectedStatus.addEventListener('change', () => {
    switch (selectedStatus.value) {
        case 'lettres':
            inputStatus.setAttribute('value', 'lettre');
            break;
        case 'sciences':
            inputStatus.setAttribute('value', 'scientifique');
            break;
        case 'religion':
            inputStatus.setAttribute('value', 'religieux');
            break;
        case 'politique':
            inputStatus.setAttribute('value', 'politique');
            break;
        case 'loi':
            inputStatus.setAttribute('value', 'loi');
            break;
        case 'résistance':
            inputStatus.setAttribute('value', 'résistant');
            break;
        case 'militaire':
            inputStatus.setAttribute('value', 'militaire');
            break;
    }
})