from django.shortcuts import render
from .models import Product
from .cart import Cart
from django.shortcuts import render, redirect

# Create your views here.

def product_detail(request,id):
    product=Product.objects.get(id=id)
    return render(request,'product_detail.html',{'product':product})
#Add to Cart
def add_to_cart(request,id):
    cart=Cart(request)
    product=Product.objects.get(id=id)
    cart.add(product)
    return redirect("cart_page")
#Remove from Cart
def remove_from_cart(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_page")
#Update Quantity
def update_quantity(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    quantity = int(request.POST.get("quantity"))
    cart.update(product, quantity)
    return redirect("cart_page")
#Cart Page (Display Items)
def cart_page(request):
    cart = Cart(request)

    cart_items = []
    for product_id, item in cart.cart.items():
        product = Product.objects.get(id=product_id)
        cart_items.append({
            "product": product,
            "quantity": item["quantity"],
            "subtotal": int(item["quantity"]) * float(item["price"])
        })

    total = cart.get_total()

    return render(request, "cart.html", {"cart_items": cart_items, "total": total})

