from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from movies.models import Movie
from django.contrib.auth.models import User


# Create your views here.

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    messages.info(request, 'Disabled Account')

            else:
                messages.warning(request, 'Sifre veya Username Hatali!!')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Basariyla kayit oldunuz,Giris yapabilirsiniz')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('index')


@login_required(login_url='login')
def user_dashboard(request):
    current_user = request.user
    movies = current_user.favorite_film.all()
    context = {
        'movies': movies,
    }
    return render(request, 'userprofile.html', context)


def favorite_film(request):
    movie_id = request.POST['movie_id']
    user_id = request.POST['user_id']
    movie = Movie.objects.get(id=movie_id)
    user = User.objects.get(id=user_id)
    movie.kullanici.add(user)
    messages.success(request, 'Favorinize Eklendiniz')
    return redirect('favorite_list')


def favorite_film_delete(request):
    movie = Movie.objects.get(id=request.POST['movie_id'])
    user = User.objects.get(id=request.POST['user_id'])
    movie.kullanici.remove(user)
    messages.warning(request, 'Favoriden Sildiniz !!!!!!')
    return redirect('favorite_list')


@login_required(login_url='login')
def favorite_list(request):
    current_user = request.user
    movies = current_user.favorite_film.all()
    context = {
        'movies': movies,
    }
    return render(request, 'userfavoritelist.html', context)
