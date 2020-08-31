from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart(object):
    # init cart object
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save empty cart in session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    # add item to cart or update quantity
    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    # remove item from cart
    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

   # total price of all items in cart
    def get_total_price(self):
        total_price = 0
        for item in self.cart.values():
            total_price += Decimal(item['quantity'] * item['price'])
        return total_price

    # clear cart
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def save(self):
        # mark session as modified
        self.session.modified = True

    def __iter__(self):
        product_ids = self.cart.keys()
        # get products by id
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
        yield item

    def __len__(self):
        # count of products in cart
        total_count = 0
        for item in self.cart.values():
            total_count += item['quantity']
        return total_count