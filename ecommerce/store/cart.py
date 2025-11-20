from django.conf import settings
from .models import Product


class Cart:
    def __init__(self,request):
        self.session=request.session
        cart=self.session.get('cart')
        if not cart:
            cart=self.session['cart']={}
        self.cart=cart
    #add to cart
    def add(self,product):
        product_id=str(product.id)
        if product_id not in self.cart:
            self.cart[product_id]={'quantity':1, "price":str(product.price)}
        else:
            self.cart[product_id]['qty']+=1
        self.save()

    def save(self):
        self.session['cart']=self.cart
        self.session.modified=True
    #remove from cart
    def remove(self,product):
        product_id=str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save() 
    #update quantity
    def update(self,product,quantity):
        product_id=str(product.id)
        if product_id in self.cart:
            self.cart[product_id]["quantity"]=quantity
            self.save()
    #calculate total
    def get_total(self):
        total=0
        for item in self.cart.values():
            total+=int(item["quantity"])*float(item["price"])
        return total            

