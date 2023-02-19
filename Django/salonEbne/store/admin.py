from django.contrib import admin
from store.models import Product, Cashier

# Register your models here.
#admin.site.register(Product)
#admin.site.register(Cashier)


# Administration of Order and Sales

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'product_name', 'quantity', 'total_price')
    list_filter = ('customer_name', 'product_name')

    def customer_name(self, obj):
        return obj.customer.name

    customer_name.short_description = 'Customer'

    def product_name(self, obj):
        return obj.product.name

    product_name.short_description = 'Product'


class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_price', 'created_at')
    list_filter = ('created_at',)
