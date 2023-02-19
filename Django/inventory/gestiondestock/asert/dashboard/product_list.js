$(document).ready(function() {
    $.ajax({
        url: '/product_list/',
        dataType: 'json',
        success: function(data) {
            var productList = $('#product-list');
            for (var i = 0; i < data.length; i++) {
                var product = data[i];
                var listItem = $('<li>').addClass('list-group-item');
                listItem.append($('<h2>').addClass('mb-1').text(product.name));
                listItem.append($('<p>').addClass('mb-1').text(product.description));
                listItem.append($('<p>').addClass('mb-1').text('Price: $' + product.price.toFixed(2)));
                listItem.append($('<p>').addClass('mb-0').text('Stock: ' + product.stock));
                productList.append(listItem);
            }
        },
        error: function() {
            alert('An error occurred while loading the product list.');
        }
    });
});
