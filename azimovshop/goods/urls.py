from django.urls import path

from .views import index, good_info, category_list, category_detail

app_name = 'goods'

urlpatterns = [
    path('', index, name='index'),
    path('good/<int:pk>/', good_info, name='good_info'),
    path('category/', category_list, name='category_list'),
    path('category/<slug>/', category_detail, name='category_detail')
]
