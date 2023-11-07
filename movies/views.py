from django.shortcuts import render, get_object_or_404,redirect
from .models import Category, Movie, Comment

from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib import messages
from django.views.generic.detail import DetailView


# Create your views here.


class MovieList(ListView):
    model = Movie
    template_name = 'movielist.html'
    context_object_name = 'films'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


def detail_movie(request, slug):
    movie = Movie.objects.get(slug=slug)
    movies = Movie.objects.all()
    current_user = request.user
    if current_user.is_authenticated:
        fav_movies = current_user.favorite_film.all()
    else:
        fav_movies = movies
    context = {
        'movie': movie,
        'fav_movies': fav_movies,
    }
    return render(request, 'moviesingle.html', context)


def category_list(request, category_slug):
    films = Movie.objects.all().filter(categories__slug=category_slug)
    category = Category.objects.all()
    context = {
        'films': films,
        'category': category
    }
    return render(request, 'movielist.html', context)


def addComment(requrest, slug):
    movie = get_object_or_404(Movie, slug=slug)
    if requrest.method == "POST":
        comment_author = requrest.POST.get('comment_author')
        comment_content = requrest.POST.get('comment_content')

        newComment=Comment(comment_author=comment_author,comment_content=comment_content)
        newComment.movie=movie
        newComment.save()
        messages.success(requrest, 'Yorunuz Eklendi.Tesekkur Ederiz :)')
        return redirect('/movies/' + slug)
    return redirect('/movies/' + slug)
