from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse_lazy



class Contact(models.Model):
    name = models.CharField(max_length=180)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=180)
    message = models.TextField()
    
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        
    def __str__(self):
        return self.name
    
    
class Blog(models.Model):
    title = models.CharField(max_length=180)
    slug = models.SlugField()
    date = models.DateField()
    image = models.ImageField(upload_to="blog/")
    description = HTMLField()
    
    def get_absolute_url(self):
        return reverse_lazy("web:blog_detail", kwargs={"slug": self.slug})
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
    
    
class Banner(models.Model):
    title = models.CharField(max_length=180, blank=True, null=True)
    sub_title = models.CharField(max_length=180, blank=True, null=True)
    image = models.ImageField(upload_to="banner/")
    
    def __str__(self):
        return self.title if self.title else f"Banner {self.id}"

    
    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'
    

class Testimonial(models.Model):
    name = models.CharField(max_length=180)
    position = models.CharField(max_length=180)
    content = models.TextField()
    
    def str(self):
        return self.name
    
    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
        

class Brand(models.Model):
    name = models.CharField(max_length=180)
    image = models.ImageField(upload_to="brand/")  
    
    def str(self):
        return self.name
    
    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
        
    