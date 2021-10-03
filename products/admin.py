from django.contrib import admin

from products.models import ProductCategory, Product

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'is_active')
    fields = ('name', 'image', 'description', ('price', 'quantity'), 'category')
    readonly_fields = ('description',)
    ordering = ('-name',)
    search_fields = ('name',)


@admin.register(ProductCategory)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    ordering = ('-name',)
    search_fields = ('name',)
