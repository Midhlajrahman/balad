// add cart ajax
$(".add-cart-btn").click(function () {
    var product= $(this).data("product-id");
    console.log('product==',product)
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
                    <i class="fa fa-credit-card"></i>
                `,
                cancelButtonAriaLabel: "Checkout",
                timer: 5000, 
                timerProgressBar: true
            }).then((result) => {
                if (result.isConfirmed) {
                    // Redirect to the view cart page
                    window.location.href = '/shop/cart/';
                } else if (result.dismiss === Swal.DismissReason.cancel) {
                    // Redirect to the checkout page
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