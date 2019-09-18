$(document).ready(function(){
    // $('#date').mask('00-00-0000');
    $('#phone').mask('+375(00)000-00-00');
});
function validationAll() {
    if (
        document.getElementById("phone").classList.contains('is-valid')
        && document.getElementById("first_name").classList.contains('is-valid')
        && document.getElementById("delivery_date").classList.contains('is-valid')
        && document.getElementById("delivery_time").classList.contains('is-valid')
        && document.getElementById("address").classList.contains('is-valid')
    ) {
        document.getElementById("order-submit").disabled = false;
    } else {
        document.getElementById("order-submit").disabled = true;
    }
}
validationAll();


function validateField(field, fieldId, count) {
    if (field.length < count) {
        document.getElementById(fieldId).className = 'form-control is-invalid';
        validationAll();
    } else {
        document.getElementById(fieldId).className = 'form-control is-valid';
        validationAll();
    }
}

function validatePhone() {
    let phoneMasked = document.getElementById("phone").value;
    var thenum = phoneMasked.match(/\d+/g).map(Number);
    var thenumSh = thenum.shift();
    phoneMasked = thenum.join('');
    validateField(phoneMasked, "phone", 9);
}

function validateDate() {
    let dateField = document.getElementById("delivery_date").value;
    validateField(dateField, "delivery_date", 1);
}

function validateTime() {
    validTime = document.querySelector('#delivery_time').value;
    validateField(validTime, "delivery_time", 2);
}

function validateAddress() {
    let address = document.getElementById("address").value;
    validateField(address, "address", 5);
}

function validateName() {
    let nameField = document.getElementById("first_name").value;
    validateField(nameField, "first_name", 3);
}

function phoneNumberToDigits() {
    let phoneMasked = document.getElementById("phone").value;
    var thenum = phoneMasked.match(/\d+/g).map(Number);
    var thenumSh = thenum.shift();
    document.getElementById('phone').value = thenum.join('');
}

let submitBtn = document.getElementById('order-submit');
submitBtn.addEventListener('click', function(event){
    event.preventDefault();
    let order = localStorage.getItem('order');
    phoneNumberToDigits();
    let form = new FormData(document.querySelector("#order-form"));
    form.append("order", order);
    postData("/order/", form);
});

function postData(url = '', data = {}) {
    return fetch(url, {
        method: 'POST',
        redirect: 'manual',
        body: data,
    })
       .then(localStorage.clear())
       .then(response => {window.location="/"});
}





