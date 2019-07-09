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

    var request = new XMLHttpRequest();
    request.open("POST", "/order/");
    request.send(form);
});
