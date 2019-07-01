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

        this.showPrice = this.showPrice.bind(this);

        $(this.sizeBtnSelector).on('click', this.showPrice);
    }

    showPrice (event) {
        let sizeBtn = $(event.target);
        let pizza = sizeBtn.closest(this.itemSelector);
        let priceArea = pizza.find(".calculator");
        let data = pizza.data();
        $.extend(data, sizeBtn.data());
        let sizeButtons = pizza.find(this.sizeBtnSelector);

        sizeButtons.removeClass('active');
        sizeBtn.addClass('active');

        priceArea.html(`<td>${data.price}</td>`);
    }
}


// Document ready logic
$(function () {

    let filter = new Filter('#category-filter .btn', '#catalog .filterDiv');
    filter.filterSelection('all');  // do initial filtering

    new Pizza();
});
