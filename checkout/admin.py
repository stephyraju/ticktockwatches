from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.
'''
TabularInline subclass defines the template used to render the
order in the admin interface.
'''
class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem

'''
The admin interface has the hability to edit more than one model
on a single page. This is know as inlines
'''
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )

admin.site.register(Order, OrderAdmin)