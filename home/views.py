from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.utils import timezone
from django.conf import settings
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib import auth, messages

 # Create your views here.
def view_about(request):
    """A View that renders the about page"""
    return render(request, "about.html")

def view_delivery(request):
    """A View that renders the delivery policy page"""
    return render(request, "delivery.html")

def view_return(request):
    """A View that renders the reurn policy page"""
    return render(request, "return.html")

def view_faqs(request):
    """A View that renders the FAQs page"""
    return render(request, "faqs.html")

def view_contact(request):
    '''Returns the contact us form page'''
    if request.user.is_authenticated:
        initial_data = {
            'name': request.user.first_name,
            'email': request.user.email
        }

        contact_form = ContactForm(initial=initial_data)
        
        if request.method == 'POST':
            contact_form = ContactForm(request.POST)

            if contact_form.is_valid():
                message = request.POST['message']
                email_from = request.user.email
                recipient_list = ['stephyraju@gmail.com']
                send_mail ( message, email_from, recipient_list)
                
                fail_silently=False
                
                messages.success(request, 
                                "Your message has been sent!",
                                extra_tags="alert-success")
                return redirect(reverse('contact'))
        else:
            messages.error(request, "Unable to send message at this time",
                                    extra_tags="alert-danger")
    else:
        contact_form = ContactForm()
   
    print()
    return render(request, 'contact.html', {'contact_form':contact_form})
    