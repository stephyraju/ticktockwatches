from django.conf.urls import url, include
from .views import view_featured, all_products2, product_detail, view_menswatch, view_rolex


urlpatterns = [
    url(r'^$', view_featured, name='index'),
    url(r'^$', all_products2, name='all_products2'),
    url(r'^view_menswatch/$', view_menswatch, name='menswatch'),
    url(r'^view_rolex/$', view_rolex, name='rolex'),
    url(r'^(?P<pk>\d+)/$', product_detail, name='product_detail'),
]