# Generated by Django 4.2.6 on 2023-11-08 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_movie_youtube_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='youtube_link',
            field=models.URLField(blank=True),
        ),
    ]
