from django.contrib import admin

from .models import Product, ParametersInProduct, Category, Parameter


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(ParametersInProduct)

