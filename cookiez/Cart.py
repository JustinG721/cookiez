from cookiez.models import ShoppingCart, Cookie

def addToCart(customerID, cookieID, count):
    cart = ShoppingCart(custid=customerID, cookieID=cookieID, quantity=count)
    cart.save()
