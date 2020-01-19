from django.conf.urls import url
from .views import  view_about 

urlpatterns = [
    url(r'^about/$', view_about, name='about')
]