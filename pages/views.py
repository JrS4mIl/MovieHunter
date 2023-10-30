from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def movie_list(request):
    return render(request, 'movielist.html')


def handling_404(request, exception=None):
    return render(request, '404.html', status=404)
