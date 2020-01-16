from django.conf.urls import url, include
from .views import all_products, all_products2, product_detail, view_menswatch


urlpatterns = [
    url(r'^$', all_products, name='index'),
    url(r'^$', all_products2, name='all_products2'),
    url(r'^view_menswatch/$', view_menswatch, name='menswatch'),
    url(r'^(?P<pk>\d+)/$', product_detail, name='product_detail'),
]