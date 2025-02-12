from django.contrib import admin

from .models import Contact, Blog, Banner, Testimonial, Brand


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'date',)
    
    
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title',)
    

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name',)
    

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)