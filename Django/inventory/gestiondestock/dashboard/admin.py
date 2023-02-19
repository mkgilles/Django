from django.contrib import admin

from dashboard.models import Product, Order

admin.site.site_header = 'Gestion de stock du salon Ebene'


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('reference', 'name', 'category', 'stock')
    list_filter = ('category',)


admin.site.register(Product, ProductAdmin),
# admin.site.register(Order)
