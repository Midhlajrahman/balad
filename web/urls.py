from django.urls import path
from . import views

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("products/", views.product, name="product"),
    path("product/<slug:slug>/", views.product_detail, name="product_detail"),
    path("blogs", views.blog, name="blog"),
    path("blog/<slug:slug>/", views.blog_detail, name="blog_detail"),
    path("contact/", views.contact, name="contact"),
     # CART
    path("shop/cart/", views.cart_view, name="cart"),
    path("shop/cart/add/", views.cart_add, name="add_cart"),
    path(
        "shop/cart-item-clear/<str:item_id>/",
        views.clear_cart_item,
        name="clear_cart_item",
    ),
    path("shop/cart-minus/", views.minus_to_cart, name="minus_to_cart"),
    path("shop/cart-clear/", views.clear_cart, name="clear_cart"),
    
    ]