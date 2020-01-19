from django.shortcuts import render

# # Create your views here.
def view_about(request):
    """A View that renders the about page"""
    return render(request, "about.html")
