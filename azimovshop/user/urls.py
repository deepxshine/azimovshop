# user/urls
from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import SignUp

app_name = 'user'

urlpatterns = [
    path('logout/', LogoutView.as_view(template_name='user/logout.html'),
         name='logout'),
    path('signup/', SignUp.as_view(), name='signup'),
]
