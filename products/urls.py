from django.conf.urls import url, include
from .views import view_index, all_products2, product_detail, view_menswatch, view_ladieswatch, view_kidswatch, view_rolex, view_timex, view_tedbaker, view_tissot, view_michaelkors,view_lacoste, view_lorus, view_citizen



urlpatterns = [
    url(r'^$', view_index, name='index'),
    url(r'^products_list/$', all_products2, name='all_products2'),
    url(r'^view_menswatch/$', view_menswatch, name='menswatch'),
    url(r'^view_ladieswatch/$', view_ladieswatch, name='ladieswatch'),
    url(r'^view_kidswatch/$', view_kidswatch, name='kidswatch'),
    url(r'^view_rolex/$', view_rolex, name='rolex'),
    url(r'^view_timex/$', view_timex, name='timex'),
    url(r'^view_tedbaker/$', view_tedbaker, name='tedbaker'),
    url(r'^view_tissot/$', view_tissot, name='tissot'),
    url(r'^view_michaelkors/$', view_michaelkors, name='michaelkors'),
    url(r'^view_lacoste/$', view_lacoste, name='lacoste'),
    url(r'^view_lorus/$', view_lorus, name='lorus'),
    url(r'^view_citizen/$', view_citizen, name='citizen'),
    url(r'^(?P<pk>\d+)/$', product_detail, name='product_detail')
]