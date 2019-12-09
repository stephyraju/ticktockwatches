from django.shortcuts import render, redirect, reverse
from django.contrib import auth

# Create your views here.
def logout(request):
    def logout(request):
    '''Log the user out / request contains the user object'''
    auth.logout(request)
    messages.success(request,'You have been succesfully loged out')
    return redirect (reverse('index'))
