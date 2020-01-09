from django.conf.urls import url, include
from .views import all_products, all_products2


urlpatterns = [
    url(r'^$', all_products, name='index'),
    url(r'^$', all_products2, name='all_products2')
]