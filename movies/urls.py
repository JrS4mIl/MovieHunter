from django.urls import path
from .views import MovieList,detail_movie
urlpatterns = [
    path('', MovieList.as_view(), name='movielist'),
    path('<slug:slug>',detail_movie, name='detail'),
]
