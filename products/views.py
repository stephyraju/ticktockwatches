from django.shortcuts import render
from .models import Product

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})

def all_products2(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})