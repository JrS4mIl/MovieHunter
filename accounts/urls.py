from django.urls import path
from .views import login_user, register, user_logout, user_dashboard, favorite_film, favorite_list,favorite_film_delete

urlpatterns = [
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('dashboard/', user_dashboard, name='dashboard'),
    path('favorite-film/', favorite_film, name='favorite_film'),
    path('favoritelist-film/', favorite_list, name='favorite_list'),
    path('favorite_film_delete/', favorite_film_delete, name='favorite_film_delete'),
]
