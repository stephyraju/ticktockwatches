from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Product
from favourites.models import Favourites
from django.http import HttpResponseRedirect
from django.conf import settings
from favourites.views import add_remove_favourites

# Create your views here.
# def all_products(request):
#     products = Product.objects.all()
#     return render(request, "index.html", {"products": products})

def all_products2(request):
    favourites = Favourites.objects.filter(user=request.user)
    products = Product.objects.all()
    paginator = Paginator(products, 8)  # Show 8 products per page
    
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, "products.html", {"products": products,
                                            'favourites':[favourite.product for favourite in favourites]})
    
def view_menswatch(request):
    """View to display only Mens"""
    products = Product.objects.all().filter(category='Mens Watches')
    paginator = Paginator(products, 8)  # Show 8 products per page
    
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "products.html", {"products": products})

def view_ladieswatch(request):
    """View to display only Ladies Watches"""
    products = Product.objects.all().filter(category='Ladies Watches')
    paginator = Paginator(products, 8)  # Show 8 products per page
    
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "products.html", {"products": products})

def view_kidswatch(request):
    """View to display only Kids Watches"""
    products = Product.objects.all().filter(category='Kids Watches')
    paginator = Paginator(products, 8)  # Show 8 products per page
    
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "products.html", {"products": products})

def view_rolex(request):
    """View to display only Rolex"""
    products = Product.objects.all().filter(brand='Rolex')
    return render(request, "products.html", {"products": products})

def view_timex(request):
    """View to display only Timex"""
    products = Product.objects.all().filter(brand='Timex')
    paginator = Paginator(products, 8)  # Show 8 products per page
    
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "products.html", {"products": products})

def view_tedbaker(request):
    """View to display only Ted Baker"""
    products = Product.objects.all().filter(brand='Ted Baker')
    paginator = Paginator(products, 8)  # Show 8 products per page
    
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "products.html", {"products": products})

def view_tissot(request):
    """View to display only Tissot"""
    products = Product.objects.all().filter(brand='Tissot')
    paginator = Paginator(products, 8)  # Show 8 products per page
    
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "products.html", {"products": products})

def view_michaelkores(request):
    """View to display only Michael Kores"""
    products = Product.objects.all().filter(brand='Michael Kores')
    paginator = Paginator(products, 8)  # Show 8 products per page
    
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "products.html", {"products": products})

def view_lacoste(request):
    """View to display only Lacoste"""
    products = Product.objects.all().filter(brand='Lacoste')
    paginator = Paginator(products, 8)  # Show 8 products per page
    
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "products.html", {"products": products})

def view_lotus(request):
    """View to display only Lotus"""
    products = Product.objects.all().filter(brand='Lotus')
    paginator = Paginator(products, 8)  # Show 8 products per page
    
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "products.html", {"products": products})

def view_citizen(request):
    """View to display only Citizen"""
    products = Product.objects.all().filter(brand='Citizen')
    paginator = Paginator(products, 8)  # Show 8 products per page
    
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
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