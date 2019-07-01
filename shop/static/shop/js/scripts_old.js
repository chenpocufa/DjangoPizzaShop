$(function() {  // called when document is ready
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

  // selection buttons script
  let selectBtn = $('#selection .btn');

  selectBtn.on('click', function(){
    let select_btn = $(this);
    var product_id = select_btn.data("product_id");
    var product_price = select_btn.data("product_price");
    localStorage.setItem(product_id, product_price);
    console.log(localStorage);

  });

  // number of items in the basket
  $('#cart a').append('<a>'+' ('+localStorage.length+' pizzas)'+'</a>');

  // cart table
  var data = {
    k: ['#', 'Item', 'Price'],
    v: []
    }

  for(var i =0; i < localStorage.length; i++){
        data.v.push([i+1, localStorage.key(i), localStorage.getItem(localStorage.key(i))]);
        }

    function Table() {
    //sets attributes
        this.header = [];
        this.data = [[]];
        this.tableClass = ''
    }

    Table.prototype.setHeader = function(keys) {
    //sets header data
    this.header = keys
    return this
    }

  Table.prototype.setData = function(data) {
      //sets the main data
    this.data = data
    return this
    }

    Table.prototype.setTableClass = function(tableClass) {
        //sets the table class name
        this.tableClass = tableClass
        return this
    }

    Table.prototype.build = function(container) {

        //default selector
        container = container || '.table-container'

        //creates table
        var table = $('<table></table>').addClass(this.tableClass)

        var tr = $('<tr></tr>') //creates row
        var th = $('<th></th>') //creates table header cells
        var td = $('<td></td>') //creates table cells

        var header = tr.clone() //creates header row

        //fills header row
        this.header.forEach(function(d) {
            header.append(th.clone().text(d))
        })

        //attaches header row
        table.append($('<thead></thead>').append(header))

        //creates
        var tbody = $('<tbody></tbody>')

        //fills out the table body
        this.data.forEach(function(d) {
            var row = tr.clone() //creates a row
            d.forEach(function(e,j) {
                row.append(td.clone().text(e)) //fills in the row
            })
            tbody.append(row) //puts row on the tbody
        })

        $(container).append(table.append(tbody)) //puts entire table in the container

        return this
    }

    //creates new table object
    var table = new Table()

    //sets table data and builds it
    table
        .setHeader(data.k)
        .setData(data.v)
        .setTableClass('sean')
        .build()
});
