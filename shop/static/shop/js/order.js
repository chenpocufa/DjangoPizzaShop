


//$(function () {
//    $('#order-submit').on('click', function(event){
//        event.preventDefault();
//        let order = localStorage.getItem('order');
//        let form = new FormData(document.querySelector("#order-form"));
//
//        form.append("order", order);
//
//        $.ajax({
//            url: "/order/",
//            type: "POST",
//            data: form,
//            processData: false,  // tell jQuery not to process the data
//            contentType: false   // tell jQuery not to set contentType
//        });
//    });
//});

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
