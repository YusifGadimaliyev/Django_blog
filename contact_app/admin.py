from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['email']


admin.site.register(Contact, ContactAdmin)

# Register your models here.
