from django.urls import path

from .views import index, good_info

app_name = 'goods'

urlpatterns = [
    path('', index, name='index'),
    path('good/<int:pk>/', good_info, name='good_info')
]
