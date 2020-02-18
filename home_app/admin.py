from django.contrib import admin
from .models import Post, useful

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_date']


admin.site.register(Post, PostAdmin)
admin.site.register(useful)
