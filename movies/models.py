from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here
#

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)  # Oluşturulma tarihi
    update_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=50, unique=True, null=True)
    description = models.TextField()
    categories = models.ManyToManyField(Category, related_name='film_category')
    kullanici=models.ManyToManyField(User,blank=True,related_name='favorite_film')
    releasedate = models.DateField()
    director = models.CharField(max_length=100)
    image = models.ImageField(upload_to='movie_image')
    hours = models.DurationField()
    puan = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    creation_date = models.DateTimeField(auto_now_add=True)  # Oluşturulma tarihi
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Movie, self).save(*args, **kwargs)


class IndexMovie(models.Model):
    youtube_link = models.URLField()
    image = models.ImageField(upload_to='movie_image')
    name = models.CharField(max_length=50)
    sure = models.FloatField()

    def __str__(self):
        return self.name
