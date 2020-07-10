from django.contrib import admin
from .models import *



class ImageAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'desc',
        'cate',
        'added_date',
        'image'

    )
    search_fields = ('title',)
    list_filter = ('cate',)

# Register your models here.
admin.site.register(Category)
admin.site.register(Image, ImageAdmin)

