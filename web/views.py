from django.shortcuts import render
from products.models import Category, Product

def index(request):
    product_categories = Category.objects.all()
    context = {
        "is_index": True, 
        "product_categories":product_categories
               }
    return render(request, "web/index.html", context)


def product(request):
    products = Product.objects.all()
    context = {
        "is_product":True,
        "products":products
    }
    return render(request, "web/product.html", context)


def about(request):
    context = {
        "is_about": True
    }
    return render(request, "web/about.html", context)


def product_detail(request):
    context = {
        "is_index":True
    }
    return render(request, "web/product-details.html", context)


def blog(request):
    context = {
        "is_blog":True
    }
    return render(request, "web/blog.html", context)


def blog_detail(request):
    context = {
        "is_blog_detail":True
    }
    return render(request, "web/blog-details.html", context)


def contact(request):
    context = {"is_contact": True}
    return render(request, "web/contact.html", context)