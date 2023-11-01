from django.shortcuts import render
from movies.models import Category, IndexMovie, Movie
from .models import GeneralSetting, ImageSetting


# Create your views here.
def index(request):
    header_movie = Movie.objects.get(title='Terminator 5 Yaradılış')
    site_title = GeneralSetting.objects.get(title='site_title').paramater

    footer_logo = ImageSetting.objects.get(name='footer_logo').file
    indexMovie = IndexMovie.objects.all()
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'indexMovie': indexMovie,
        'site_title': site_title,
        'footer_logo': footer_logo,
        'header_moive': header_movie,
        'header_movie': header_movie,
    }
    return render(request, 'index.html', context)
