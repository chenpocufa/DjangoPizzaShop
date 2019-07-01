$(function() {
      // filter script
  let categoryBtn = $('#category-filter .btn');
  let items = $('#catalog .filterDiv');

  categoryBtn.on('click', function(){
    let clickedBtn = $(this);  // wrap `this` to be able to call jquery methods
    let activeBtn = $('.btn.active');
    activeBtn.removeClass('active');
    clickedBtn.addClass('active');

    let category = clickedBtn.attr('filter');
    filterSelection(category);
  });

  let filterSelection = function(categoryName) {
  	// if show all, add `show` class to all items and return
    if (categoryName === 'all') {
      items.addClass('show');
      return;
    }

    // hide all by default
    items.removeClass('show');

    // show only items which have `categoryName` class
  	items.map(function(idx, item){
      let elem = $(item);
      if (elem.hasClass(categoryName)){
        elem.addClass('show');
      }
    });
  };

  // do initial filtering
  filterSelection('all');

let sizeBtn = $('#selection .btn');

  sizeBtn.on('click', function(){
      let selBtn = $(this);
      let selInfo = [{
        'id': selBtn.data('id'),
        'name': selBtn.data('name'),
        'size': selBtn.data('size'),
        'price': selBtn.data('price'),
        'quantity': 1}
        ]
      console.log(selInfo)

      $(".calculator").data("item-price", selInfo[0].price);
      $(".calculator #sel-price").text($(".calculator").data("item-price"));
      })

});
