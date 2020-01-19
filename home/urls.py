from django.conf.urls import url
from .views import  view_about, view_delivery, view_return, view_faqs

urlpatterns = [
    url(r'^about/$', view_about, name='about'),
    url(r'^delivery/$', view_delivery, name='delivery'),
    url(r'^return/$', view_return, name='return'),
    url(r'^faqs$', view_faqs, name='faqs')
]