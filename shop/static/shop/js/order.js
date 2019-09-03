$(document).ready(function(){
    // $('#date').mask('00-00-0000');
    $('#phone').mask('(00)000-00-00');
});

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

//     let submitBtn = document.getElementsByClassName('order-submit');
//     submitBtn.addEventListener('click', {function(event) {
//        event.preventDefault();
//        let order = localStorage.getItem('order');
//        let form = new FormData(document.querySelector("#order-form"));
//        form.append("order", order);
//        postData("/order/", form);
//     }});


function addThisOrder (){
    let order = localStorage.getItem('order');
    let form = new FormData(document.querySelector("#order-form"));
    alert(form);
    form.append("order", order);
    debugger;
    postData("/order/", form);
};
//  'id': 'phone', , 'id': 'text', 'id': 'time', 'id': 'address', 'id': 'comment'

function postData(url = '', data = {}) {
    alert(data);
    return fetch(url, {
        method: 'POST',
        redirect: 'manual',
        body: data,
    })

        .then(localStorage.clear())
        .then(response => {window.location="/"});
}





