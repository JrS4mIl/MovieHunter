from django.shortcuts import render
from .models import Category, Movie

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


# Create your views here.


class MovieList(ListView):
    model = Movie
    template_name = 'movielist.html'
    context_object_name = 'films'
    paginate_by = 8


def detail_movie(request, slug):
    movie = Movie.objects.get(slug=slug)
    context = {
        'movie': movie,
    }
    return render(request, 'moviesingle.html', context)
