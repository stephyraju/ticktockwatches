from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm, UserUpdateForm

# Create your views here.

def index(request):
    '''Return the home page'''
    return render(request, 'index.html')

@login_required
def logout(request):
    '''Log out the user / request contains the user object'''
    auth.logout(request)
    messages.success(request,'You have been succesfully loged out')
    return redirect (reverse('index'))

def login(request):
    """Return a login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


def registration(request):
    '''Registration page'''
   
    '''If the user is already logged in it redirects them to the index page'''

    if request.user.is_authenticated:
        return redirect(reverse('index'))
        
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        
        if registration_form.is_valid():
            registration_form.save()
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(request=request, user=user)
                messages.success(request, 'You have been succesfully registered')
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to register your account at this time")
    
        
    else:
            registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {
            "registration_form": registration_form})

def user_profile(request):
    """The user's profile page"""
    user_profile = User.objects.get(email=request.user.email)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, u'Your account info has been updated.')
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'profile.html', {'form':form,
                                            'user_profile':user_profile})