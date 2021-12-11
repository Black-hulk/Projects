from django.contrib import admin
from .models import Products, Order
# Register your models here.
admin.site.site_header= "Simple E-commerce Site"
admin.site.site_title="E-commerce Shoping"
admin.site.index_title="Admin Panel Of E-commerce Shoping"

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','price', 'discount_price', 'category', 'description')
    search_fields = ('title',)
    list_editable=('price','discount_price','category',)
admin.site.register(Products,ProductAdmin)
admin.site.register(Order)
