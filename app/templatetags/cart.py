from django import template
from numpy import False_

register =  template.Library()

@register.filter(name="isexistincart")
def iseixstincart(product,cart):
    keys = cart.keys()
    print(keys)
    for id in keys:
        if int(id)==product.id:
            return True
    return False

@register.filter(name="cartquant")
def cartquant(product,cart):
    keys = cart.keys()
    print(keys)
    for id in keys:
        if int(id)==product.id:
            return cart.get(id)
            
    return False
@register.filter(name="total_price")
def total_price(product, cart):
    return product.price * cartquant(product, cart)

@register.filter(name="grand_total")
def grand_total(products,cart):
    sum=0
    for i in products:
        sum+=total_price(i,cart)
    return sum

@register.filter(name="multiplyprice")
def multiplyprice(num1,num2):
    return num1*num2