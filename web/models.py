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
    