$(document).ready(function(){
    $('#birth-date').mask('00-00-0000');
    $('#phone').mask('(00)000-00-00');
});

let submitBtn = document.getElementById('order-submit');
submitBtn.addEventListener('click', function(event){
    event.preventDefault();
    let order = localStorage.getItem('order');
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






