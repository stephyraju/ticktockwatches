from django.shortcuts import render
from .models import Product

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})

def all_products2(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

def view_menswatch(request):
    """View to display only Mens"""
    products = Product.objects.all().filter(category='Mens Watches')
    return render(request, "products.html", {"products": products})

def view_ladieswatch(request):
    """View to display only Ladies Watches"""
    products = Product.objects.all().filter(category='Ladies Watches')
    return render(request, "products.html", {"products": products})

def view_kidswatch(request):
    """View to display only Kids Watches"""
    products = Product.objects.all().filter(category='Kids Watches')
    return render(request, "products.html", {"products": products})

def view_rolex(request):
    """View to display only Rolex"""
    products = Product.objects.all().filter(category='Rolex')
    return render(request, "products.html", {"products": products})

def view_timex(request):
    """View to display only Timex"""
    products = Product.objects.all().filter(category='Timex')
    return render(request, "products.html", {"products": products})

def view_tedbaker(request):
    """View to display only Ted Baker"""
    products = Product.objects.all().filter(category='Ted Baker')
    return render(request, "products.html", {"products": products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.save()
    return render(request, "productdetail.html", {'product': product})