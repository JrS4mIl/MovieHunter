# Generated by Django 4.2.6 on 2023-11-01 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generalsetting',
            name='footer_logo',
        ),
        migrations.RemoveField(
            model_name='generalsetting',
            name='header_logo',
        ),
        migrations.AddField(
            model_name='generalsetting',
            name='icerik',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='generalsetting',
            name='paramater',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='generalsetting',
            name='title',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]