$(function () {
    let order = JSON.parse(localStorage.getItem('order'))
        console.log(order);
        console.log(Object.keys(order).length);
        for (let i in order){
            let pizza = order[i];
            $("table").append(
                  "<tr>" +
                    `<td>${pizza.name}</td>` +
                    `<td>${pizza.size}</td>` +
                    `<td>${pizza.quantity}</td>` +
                    `<td>${pizza.quantity * pizza.price}</td>` +
                  "</tr>"
            );
});
