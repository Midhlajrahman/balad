
$(document).ready(function () {
    // Function to update prices  for a specific card
    function updatePricesAndOffer(card) {
        var selected = card.find('select[name="product_size"] option:selected');
        if (selected.length > 0) {
            var salePrice = selected.data('sale_price');
            var originalPrice = selected.data('original_price');
            card.find('.sale_price').text('₹' + salePrice);
            card.find('.original_price').text('₹' + originalPrice);
        }
    }
    // Event listener for select button click within each card
    $('select[name="product_size"]').change(function () {
        var card = $(this).closest('.card-product');
        updatePricesAndOffer(card);
    });
    // add cart ajax
    $(".cart-add-btn").click(function () {
        var card = $(this).closest('.card-product');
        var selected = card.find('select[name="product_size"] option:selected');
        var product= selected.val();
        var url = "/shop/cart/add/?product_id="+product; 
        $.ajax({
            type: "GET",
            url: url,
            success: function (data) {
                // Display success message
                $('.header_cart_count').html(data.cart_count)
                
                Swal.fire({
                    title: "<strong>Item Added to Cart</strong>",
                    icon: "success",
                    html: `
                        <p>Your item has been added to the cart successfully!</p>
                        <p>What would you like to do next?</p>
                    `,
                    showCloseButton: true,
                    showCancelButton: true,
                    focusConfirm: false,
                    confirmButtonText: `
                        View Cart
                        <i class="fa fa-shopping-cart"></i>
                    `,
                    confirmButtonAriaLabel: "View Cart",
                    cancelButtonText: `
                        Checkout
                        <i class="fa fa-credit-card" ></i>
                    `,
                    cancelButtonAriaLabel: "Checkout",
                    timer: 5000, 
                    timerProgressBar: true
                }).then((result) => {
                    if (result.isConfirmed) {
                        // Redirect to the view cart page
                        window.location.href = '/shop/cart/';
                    } else if (result.dismiss === Swal.DismissReason.cancel) {
                        window.location.href = '/checkout/';
                    }
                });
                
            },
            error: function (data) {
                
                if (data.status == '401') {
                    window.location.href = '/accounts/login/';
                } else {
                    // Display error message with SweetAlert
                    Swal.fire({
                        title: "Error",
                        icon: "error",
                        text: data.responseJSON.message || "An error occurred while adding the item to the cart."
                    });
                }
            }
        });
    });
 // add wishlist ajax
$(".wishlist-btn").click(function () {
    var product = $(this).data('product');
    var url = "/wishlist/add/?product_id=" + product;
    
    $.ajax({
        type: "GET",
        url: url,
        success: function (data) {
            // SweetAlert popup for wishlist
            Swal.fire({
                title: "<strong>Item Added to Wishlist</strong>",
                icon: "success",
                html: `
                    <p>Your item has been added to your wishlist successfully!</p>
                    <p>What would you like to do next?</p>
                `,
                showCloseButton: true,
                showCancelButton: true,
                focusConfirm: false,
                confirmButtonText: `
                    View Wishlist
                    <i class="fa fa-heart"></i>
                `,
                confirmButtonAriaLabel: "View Wishlist",
                cancelButtonText: `
                    Continue Shopping
                    <i class="fa fa-shopping-bag"></i>
                `,
                cancelButtonAriaLabel: "Continue Shopping",
                timer: 5000,
                timerProgressBar: true
            }).then((result) => {
                if (result.isConfirmed) {
                    // Redirect to the wishlist page
                    window.location.href = '/wishlist';
                } else if (result.dismiss === Swal.DismissReason.cancel) {
                    // Redirect to the home page or continue shopping
                    window.location.href = '/shop';
                }
            });
        },
        error: function (data) {
            if (data.status == '401') {
                window.location.href = '/accounts/login/';
            } else {
                // Display error message with SweetAlert
                Swal.fire({
                    title: "Error",
                    icon: "error",
                    text: data.responseJSON.message || "An error occurred while adding the item to the wishlist."
                });
            }
        }
    });
});
    });