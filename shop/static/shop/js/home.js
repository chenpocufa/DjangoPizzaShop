class Filter {

    constructor(btnSelector, itemsSelector) {
        this.btnSelector = btnSelector;
        this.itemAttrName = 'filter';

        this.categoryBtn = $(btnSelector);
        this.items = $(itemsSelector);

        this.processFilterClick = this.processFilterClick.bind(this);
        this.filterSelection = this.filterSelection.bind(this);

        this.categoryBtn.on('click', this.processFilterClick);
    }

    processFilterClick(event) {
        // Get clicked element from `event.target` as `this` is overrided by Filter object
        let clickedBtn = $(event.target);
        let activeBtn = $(this.btnSelector + '.active');
        let category = clickedBtn.attr(this.itemAttrName);

        activeBtn.removeClass('active');
        clickedBtn.addClass('active');

        this.filterSelection(category);
    }

    filterSelection (categoryName) {
        // if show all, add `show` class to all items and return
        if (categoryName === 'all') {
            this.items.addClass('show');
            return;
        }

        // hide all by default
        this.items.removeClass('show');

        // show only items which have `categoryName` class
        this.items.map(function (idx, item) {
            let elem = $(item);
            if (elem.hasClass(categoryName)) {
                elem.addClass('show');
            }
        });
    };

}


class Pizza {
    constructor() {
        this.itemSelector = '.card';
        this.sizeBtnSelector = '#size button';
        this.minusBtn = '.btn-minus';
        this.plusBtn = '.btn-plus';

        this.showPrice = this.showPrice.bind(this);

        $(this.sizeBtnSelector).on('click', this.showPrice);
    }

    showPrice (event) {
        let Btn = $(event.target);
        let pizza = Btn.closest(this.itemSelector);
        let priceArea = pizza.find(".calculator-price");
        let quantityArea = pizza.find(".calculator-quantity");
        let data = pizza.data();
        let sizeButtons = pizza.find(this.sizeBtnSelector);
        let minusButtons = pizza.find(this.minusBtn);
        let plusButtons = pizza.find(this.plusBtn);
        let calculatorPrice = data.price;

        if (Btn.is(".btn-secondary")){
            sizeButtons.removeClass('active');
            Btn.addClass('active');
            $.extend(data, Btn.data());
            priceArea.html(`${data.price}`);
            calculatorPrice = data.price * data.quantity;
            priceArea.html(`${calculatorPrice}`);
        }

        if (Btn.is(".btn-plus")){
            data.quantity = data.quantity + 1;
            quantityArea.html(`${data.quantity}`);
            calculatorPrice = data.price * data.quantity;
            priceArea.html(`${calculatorPrice}`);
        }

        if (Btn.is(".btn-minus")){
            if (data.quantity === 1){
            }
            else {
                data.quantity = data.quantity - 1;
            }
            quantityArea.html(`${data.quantity}`);
            calculatorPrice = data.price * data.quantity;
            priceArea.html(`${calculatorPrice}`);
        }

        if (Btn.is(".add-cart")){
            if (localStorage.getItem('order') === null){
                localStorage.setItem('order', JSON.stringify({}));
            }

            let order = JSON.parse(localStorage.getItem('order'));
            order[data.id] = data;
            localStorage.setItem('order', JSON.stringify(order));
        }
    }
}

// Document ready logic
$(function () {

    let filter = new Filter('#category-filter .btn', '#catalog .filterDiv');
    filter.filterSelection('all');  // do initial filtering

    new Pizza();
});
