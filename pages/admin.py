from django.contrib import admin
from .models import GeneralSetting, ImageSetting


# Register your models here.
@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'icerik', 'paramater']

    class Meta:
        model = GeneralSetting


@admin.register(ImageSetting)
class ImageSettingAdmin(admin.ModelAdmin):
    list_display = ['name', 'icerik', ]

    class Meta:
        model = ImageSetting
