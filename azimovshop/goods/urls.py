from django.urls import path

from .views import (index, good_info, category_list, category_detail, search,
                    profile_detail, add_to_cart, add_to_favorite,
                    del_from_favorite, del_from_shopping_cart, favorite_index,
                    create_review, shopping_cart_info)

app_name = 'goods'

urlpatterns = [
    path('', index, name='index'),
    path('good/<int:pk>/', good_info, name='good_info'),
    path('category/', category_list, name='category_list'),
    path('category/<slug>/', category_detail, name='category_detail'),
    path('search', search, name='search'),
    path('profile/', profile_detail, name='profile'),

    path('good/<int:pk>/add_to_cart/', add_to_cart, name='cart_add'),
    path('good/<int:pk>/del_from_cart/', del_from_shopping_cart,
         name='cart_del'),
    path('good/<int:pk>/add_to_fav/', add_to_favorite, name='fav_add'),
    path('good/<int:pk>/del_from_fav/', del_from_favorite, name='fav_del'),
    path('favorites/', favorite_index, name='favorite'),
    path('create_review/<int:pk>/', create_review, name='create_review'),
    path('shopping_cart/', shopping_cart_info, name='cart'),
]
