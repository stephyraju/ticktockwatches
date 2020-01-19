from django.shortcuts import render

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


