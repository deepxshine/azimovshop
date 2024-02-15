from django.contrib import admin

from .models import (Product, ParametersInProduct, Category, Parameter,
                     Profile, Favorite, ShoppingCart, Review)


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
    list_display = ('name', 'unit')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')


admin.site.register(ParametersInProduct)
admin.site.register(Profile)
admin.site.register(Favorite)
admin.site.register(ShoppingCart)
admin.site.register(Review)
