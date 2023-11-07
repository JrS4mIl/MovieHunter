from django.urls import path
from .views import MovieList, detail_movie, category_list,addComment

urlpatterns = [
    path('', MovieList.as_view(), name='movielist'),
    path('<slug:slug>', detail_movie, name='detail'),
    path('categories/<slug:category_slug>', category_list, name='category_list'),
    path('comment/<slug:slug>',addComment, name='comment')
]
