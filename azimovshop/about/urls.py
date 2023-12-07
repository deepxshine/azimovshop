from django.urls import path

from .views import (howtomakeorder, howtopay, qanda, rules, social_links,
                    history)

app_name = 'about'
urlpatterns = [
    path('howtomakeorder/', howtomakeorder, name='howtomakeorder'),
    path('howtopay/', howtopay, name='howtopay'),
    path('qanda/', qanda, name='qanda'),
    path('rules/', rules, name='rules'),
    path('social_links/', social_links, name='social_links'),
    path('history/', history, name='history'),
]
