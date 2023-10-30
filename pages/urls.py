from django.urls import path
from .views import index,movie_list
urlpatterns = [
    path('',index,name='index'),
    path('movies/',movie_list,name='movielist')
]