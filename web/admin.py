from django.contrib import admin
from .models import Contact, Blog


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'date',)