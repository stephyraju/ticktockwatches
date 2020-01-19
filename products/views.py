from django.shortcuts import render, get_object_or_404
from .models import Product
from django.conf import settings

# Create your views here.
# def all_products(request):
#     products = Product.objects.all()
#     return render(request, "index.html", {"products": products})

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
    products = Product.objects.all().filter(brand='Rolex')
    return render(request, "products.html", {"products": products})

def view_timex(request):
    """View to display only Timex"""
    products = Product.objects.all().filter(brand='Timex')
    return render(request, "products.html", {"products": products})

def view_tedbaker(request):
    """View to display only Ted Baker"""
    products = Product.objects.all().filter(brand='Ted Baker')
    return render(request, "products.html", {"products": products})

def view_tissot(request):
    """View to display only Tissot"""
    products = Product.objects.all().filter(brand='Tissot')
    return render(request, "products.html", {"products": products})

def view_michaelkores(request):
    """View to display only Michael Kores"""
    products = Product.objects.all().filter(brand='Michael Kores')
    return render(request, "products.html", {"products": products})

def view_lacoste(request):
    """View to display only Lacoste"""
    products = Product.objects.all().filter(brand='Lacoste')
    return render(request, "products.html", {"products": products})

def view_lotus(request):
    """View to display only Lotus"""
    products = Product.objects.all().filter(brand='Lotus')
    return render(request, "products.html", {"products": products})

def view_citizen(request):
    """View to display only Citizen"""
    products = Product.objects.all().filter(brand='Citizen')
    return render(request, "products.html", {"products": products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.save()
    return render(request, "product_detail.html", {'product': product})

def view_featured(request):
    """ Renders home page with 4 random featured products in featured listing section """

    # featured_products = Product.objects.filter(featured=True).order_by('-featured'[:4])
    # featured_products = Product.objects.filter(featured=True)
    featured_products = Product.objects.filter(featured=True).order_by('?')[:4]
    bestseller = Product.objects.filter(bestseller=True)
    context = {
        'featured_products': featured_products,
        'bestseller': bestseller,
        'category': 'All products'
    }
    return render(request, "index.html", context)