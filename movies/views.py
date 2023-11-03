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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


def detail_movie(request, slug):
    movie = Movie.objects.get(slug=slug)
    context = {
        'movie': movie,
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
