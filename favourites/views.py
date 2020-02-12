from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.models import User
from products.models import Product
from django.http import HttpResponseRedirect
from .models import Favourites
from django.contrib.auth.decorators import login_required

"""
If the Product is already added to favourite then remove it from favourites.
If the Product is not in favourite then save it as favourite
"""
"""
@login_required so only authenticated users can have favourites list of products
"""
@login_required
def view_fav(request):
    """A View that renders the cart contents page"""
    return render(request, "favourite.html")

@login_required
def add_remove_favourites(request, id):
    #working
    # product = get_object_or_404(Product, pk=id)
    # user_profile = User.objects.get(email=request.user.email)
    # favourites = Favourites.objects.filter(user=request.user)

    # # import pdb
    # # pdb.set_trace()

    # if favourites.filter(user=user_profile).exists():
    #     Favourites.objects.filter(user=user_profile).delete()
       
    # else:
    #     Favourites.objects.create(user=user_profile, product=product)

    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    # Youtube
    product = get_object_or_404(Product,pk=id)
    if product.favourite.filter(id=request.user.id).exists():
        product.favourite.remove(request.user)
    else:
        product.favourite.add(request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


    #  product = get_object_or_404(Product,pk=id)
    # if request.method == 'POST':
    #     user_profile = User.objects.get(email=request.user.email)
    #     fav_product = Product.objects.get(pk=id)
        
    #     if fav_product in user_profile.favourites.all():
    #         user_profile.favourites.remove(fav_product)
    #     else:
    #         user_profile.favourites.add(fav_product)

    
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
def favourite_list(request):
    #    favourites = Favourites.objects.filter(user=request.user)
       user = request.user
       favourite_products = user.favourite.all()
       
       return render(request, 'favourite.html', {"favourite_products": favourite_products,
                                                # 'favourites':favourites 
                                                })



    

    
     