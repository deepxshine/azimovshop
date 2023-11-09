from django.contrib import admin

from .models import Product, ParametersInProduct, Category, Parameter

class ParameterInline(admin.TabularInline):
    model = ParametersInProduct
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'count')
    list_filter = ('price', 'count', 'category')
    search_fields = ('name',)
    inlines = ParameterInline,

@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(ParametersInProduct)
