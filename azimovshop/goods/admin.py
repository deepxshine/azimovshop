from django.contrib import admin

from .models import (Product, ParametersInProduct, Category, Parameter,
                     Profile, Favorite, ShoppingCart, Review,
                     Order, ProductsInOrder)


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


class ProductsInOrderInline(admin.TabularInline):
    model = ProductsInOrder # модель, на основе которой создается инлайн
    extra = 0  # сколько пустых полей создается
    can_delete = False
    readonly_fields = ('summa', 'count', 'product', 'order')
    show_change_link = True


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (ProductsInOrderInline,)
    fields = ('id', 'user', 'status', 'summa', 'order_date')
    readonly_fields = ('id', 'user', 'summa', 'order_date')


admin.site.register(ParametersInProduct)
admin.site.register(Profile)
admin.site.register(Favorite)
admin.site.register(ShoppingCart)
admin.site.register(Review)

