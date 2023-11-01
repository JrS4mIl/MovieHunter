from django.shortcuts import render
from .models import Category, Movie
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic.list import ListView


# Create your views here.


class MovieList(ListView):
    model = Movie
    template_name = 'movielist.html'
    context_object_name = 'films'
    paginate_by = 8
