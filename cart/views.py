from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from products.models import Product
from django.contrib import messages

# Create your views here.

@login_required()
def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")

@login_required()
def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    if id in cart:
        messages.success(request, 'Watch successfully added to cart')

    request.session['cart'] = cart
    return redirect(reverse('index'))


@login_required()
def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


