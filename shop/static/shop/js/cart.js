// $(function () {
//     let order = JSON.parse(localStorage.getItem('order'))
//         console.log(localStorage);
// //        console.log(Object.keys(order).length);
//     let totalPrice = 0;
//     for (let i in order){
//         let pizza = order[i];
//         let pizzaPrice = pizza.quantity * pizza.price
//         totalPrice = totalPrice + pizzaPrice
//         $("table").append(
//               "<tr>" +
//                 `<td>${pizza.name}</td>` +
//                 `<td>${pizza.size}</td>` +
//                 `<td>${pizza.quantity}</td>` +
//                 `<td>${pizzaPrice.toFixed(2)}</td>` +
//               "</tr>"
//         )};
//     $('div .totalPrice').append(totalPrice.toFixed(2));
//
//    $(".confirm-order").click(function() {
//        localStorage.setItem('total', totalPrice);
//    });
// });








var shoppingCart = (function() {
    cart = [];

    // Constructor
    function Item(id, name, price, quantity, size) {
        this.id = id;
        this.name = name;
        this.price = price;
        this.quantity = quantity;
        this.size = size;
    }

    // Save cart
    function saveCart() {
        localStorage.setItem('order', JSON.stringify(cart));
    }

    // Load cart
    function loadCart() {
        cart = JSON.parse(localStorage.getItem('order'));
    }
    if (localStorage.getItem('order') != null) {
        loadCart();
    }


    var obj = {};

    // Add to cart
    obj.addItemToCart = function(id, size) {
        for(var item in cart) {
            if(cart[item].id === id && cart[item].size === size) {
                cart[item].quantity ++;
                saveCart();
                return;
            }
        }
        var item = new Item(id, name, price, quantity, size);
        cart.push(item);
        saveCart();
    }


    // Remove item from cart
    obj.removeItemFromCart = function(id, size) {
        for(var item in cart) {
            if(cart[item].id === id && cart[item].size === size) {
                cart[item].quantity --;
                if(cart[item].quantity === 0) {
                    cart.splice(item, 1);
                }
                break;
            }
        }
        saveCart();
    }

    // Remove all items from cart
    obj.removeItemFromCartAll = function(id, size) {
        for(var item in cart) {
            if(cart[item].id === id && cart[item].size === size) {
                cart.splice(item, 1);
                break;
            }
        }
        saveCart();
    }

    // Clear cart
    obj.clearCart = function() {
        cart = [];
        saveCart();
    }

    // Count cart
    obj.totalCount = function() {
        var totalCount = 0;
        for(var item in cart) {
            totalCount += cart[item].quantity;
        }
        return totalCount;
    }

    // Total cart
    obj.totalCart = function() {
        var totalCart = 0;
        for(var item in cart) {

            totalCart += cart[item].price * cart[item].quantity;
        }
        return Number(totalCart.toFixed(2));
    }

    // List cart
    obj.listCart = function() {
        var cartCopy = [];
        for(i in cart) {
            item = cart[i];
            itemCopy = {};
            for(p in item) {
                itemCopy[p] = item[p];

            }
            itemCopy.total = Number(item.price * item.quantity).toFixed(2);
            cartCopy.push(itemCopy)
        }
        return cartCopy;
    }

    // cart : Array
    // Item : Object/Class
    // addItemToCart : Function
    // removeItemFromCart : Function
    // removeItemFromCartAll : Function
    // clearCart : Function
    // countCart : Function
    // totalCart : Function
    // listCart : Function
    // saveCart : Function
    // loadCart : Function
    return obj;
})();

function displayCart() {
    var cartArray = shoppingCart.listCart();
    var output = "";
    for(var i in cartArray) {
        output += "<tr class='cart-row'>"
            + "<td class='align-middle'><img class=\"rounded mx-auto d-block small-Img\" src=" + cartArray[i].image + "></td>"
            + "<td class='align-middle'><div><h5>" + cartArray[i].name + "</h5><p class='font-italic'>" + cartArray[i].size + "</p></div></td>"
            + "<td class='align-middle'>" + cartArray[i].price + "</td>"
            + "<td class='align-middle'><div class='input-group'><span class='minus-item btn btn-small font-weight-bold'" +
            " data-id=" + cartArray[i].id + " data-size=" + cart[i].size + ">-</span>"
            + "<span type='number' " +
            "class='item-count font-weight-bold' data-id='" + cartArray[i].id + "'>" + cartArray[i].quantity + "</span>"
            + "<span " +
            "class='plus-item btn btn-small font-weight-bold' data-id=" + cartArray[i].id + "" +
            " data-size=" + cartArray[i].size + ">+</span></div></td>"
            + "<td class='align-middle font-weight-bold'>" + cartArray[i].total + "</td>"
            + "<td class='align-middle byn-text'>\ BYN \</td>"
            + "<td class='align-middle'><button class='delete-item' data-id=" + cartArray[i].id + "" +
            " data-size=" + cart[i].size + ">X</button></td>"
            +  "</tr>"
        ;
    }
    $('.show-cart').html(output);
    $('.total-cart').html(shoppingCart.totalCart());
    $('.total-count').html(shoppingCart.totalCount());
}

// Delete item button

$('.show-cart').on("click", ".delete-item", function(event) {
    var id = $(this).data('id');
    var size = $(this).data('size');
    shoppingCart.removeItemFromCartAll(id, size);
    displayCart();
})


// -1
$('.show-cart').on("click", ".minus-item", function(event) {
    var id = $(this).data('id');
    var size = $(this).data('size');
    shoppingCart.removeItemFromCart(id, size);
    displayCart();
})
// +1
$('.show-cart').on("click", ".plus-item", function(event) {
    var id = $(this).data('id');
    var size = $(this).data('size');
    shoppingCart.addItemToCart(id, size);
    displayCart();
})

displayCart();

$(".confirm-order").click(function() {
    var totalPrice = shoppingCart.totalCart();
    localStorage.setItem('total', totalPrice.toFixed(2));
});
