$(function () {
    let order = JSON.parse(localStorage.getItem('order'))
        console.log(localStorage);
//        console.log(Object.keys(order).length);
    let totalPrice = 0
    for (let i in order){
        let pizza = order[i];
        let pizzaPrice = pizza.quantity * pizza.price
        totalPrice = totalPrice + pizzaPrice
        $("table").append(
              "<tr>" +
                `<td>${pizza.name}</td>` +
                `<td>${pizza.size}</td>` +
                `<td>${pizza.quantity}</td>` +
                `<td>${pizzaPrice.toFixed(2)}</td>` +
              "</tr>"
        )};
    $('div .totalPrice').append(totalPrice.toFixed(2));

//    $(".confirm-order").click(function() {
//        localStorage.setItem('total', totalPrice);
//    });
});
