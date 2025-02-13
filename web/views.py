from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from django.db.models import OuterRef, Subquery

from decimal import Decimal
from django.urls import reverse


from products.models import Category, Product, AvailableSize
from products.forms import ReviewForm
from web.models import Banner, Testimonial

# CART
from web.cart import Cart


def index(request):
    product_categories = Category.objects.all()
    banners = Banner.objects.all()
    testimonials = Testimonial.objects.all()
    products = Product.objects.all()
    context = {
        "is_index": True, 
        "product_categories":product_categories,
        "banners":banners,
        "testimonials":testimonials,
        "products":products
               }
    return render(request, "web/index.html", context)


def product(request):
    sort_option = request.GET.get('sort', 'default')
    products = Product.objects.all()

    sale_price_subquery = AvailableSize.objects.filter(
        product=OuterRef('pk')
    ).order_by('sale_price').values('sale_price')[:1]

    products = products.annotate(sale_price=Subquery(sale_price_subquery))

    if sort_option == "latest":
        products = products.order_by("-id")
    elif sort_option == "best_selling":
        products = products.order_by("-is_best_seller")
    elif sort_option == "low_to_high":
        products = products.order_by("sale_price")
    elif sort_option == "high_to_low":
        products = products.order_by("-sale_price")

    context = {
        "is_product": True,
        "products": products,
        "total_products": Product.objects.count(),  
        "sort_option": sort_option,
    }
    return render(request, "web/product.html", context)


def about(request):
    context = {
        "is_about": True
    }
    return render(request, "web/about.html", context)


def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    other_products = Product.objects.exclude(slug=slug, category=product.category)
    
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)  # Don't save yet
            review.product = product  # Assign the product to the review
            review.save()  # Now save it
            response_data = {
                "is_contact": True,
                "status": "true",
                "title": "Review Submitted Successfully",
                "message": "Thank you for your review! Your feedback helps us improve.",
            }
        else:
            error_messages = {field: form.errors[field][0] for field in form.errors}
            print("Form Validation Error:", error_messages) 
            response_data = {
                "status": "false",
                "title": "Form Validation Error",
                "message": error_messages,
            }
        return JsonResponse(response_data)
    else:
        form = ReviewForm()
    
    context = {
        "is_index": True,
        "product": product,
        "other_products": other_products,
        "form": form
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


# CART
def cart_view(request):
    cart = Cart(request)
    cart_items = []

    for item_id, item_data in cart.get_cart():
        variant = get_object_or_404(AvailableSize, id=item_id)
        quantity = item_data["quantity"]
        total_price = Decimal(item_data["sale_price"]) * quantity
        cart_items.append(
            {
                "product": variant,
                "quantity": quantity,
                "total_price": total_price,
            }
        )
    context = {
        "cart_items": cart_items,
        "cart_total": sum(
            Decimal(item[1]["quantity"]) * Decimal(item[1]["sale_price"])
            for item in cart.get_cart()
        ),
    }

    return render(request, "web/cart.html", context)


def cart_add(request):
    cart = Cart(request)
    cart_instance = cart.cart
    quantity = request.GET.get("quantity", 1)
    product_id = request.GET.get("product_id", "")
    print('product_id=',product_id)
    variant = get_object_or_404(AvailableSize, pk=product_id)
    cart.add(variant, quantity=int(quantity))
    return JsonResponse(
        {
            "message": "Product Quantity Added from cart successfully",
            "quantity": cart.get_product_quantity(variant),
            "total_price": cart.get_total_price(cart_instance[product_id]),
            "cart_total": cart.cart_total(),
            "cart_count": len(cart_instance),
        }
    )


def clear_cart_item(request, item_id):
    cart = Cart(request)
    variant = get_object_or_404(AvailableSize, id=item_id)
    cart.remove(variant)
    return redirect(reverse("web:cart"))


def minus_to_cart(request):
    cart = Cart(request)
    cart_instance = cart.cart
    item_id = request.GET.get("item_id")
    variant = get_object_or_404(AvailableSize, id=item_id)
    cart.decrease_quantity(variant)
    return JsonResponse(
        {
            "message": "Product Quantity decreased from cart successfully",
            "quantity": cart.get_product_quantity(variant),
            "total_price": cart.get_total_price(cart_instance[item_id]),
            "cart_total": cart.cart_total(),
        }
    )


def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect(reverse("web:shop"))
