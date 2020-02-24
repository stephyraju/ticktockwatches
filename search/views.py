from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from products.models import Product


def do_search(request):
    """
    View for search page. Search results will be displayed in Products page
    """
    products = Product.objects.filter(title__icontains=request.GET['q'])
    paginator = Paginator(products, 4)  # Show 4 products per page
    
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "products.html", {"products": products})