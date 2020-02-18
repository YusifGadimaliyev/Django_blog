from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=33, verbose_name='Başlıq')
    content = models.TextField(verbose_name='Metn')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Tarix')
    image = models.ImageField(upload_to='images/', verbose_name='Foto')
    show = models.IntegerField(default=0, blank=True, null=True)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('home_app:post_detail', kwargs={'pk': self.id})


class useful(models.Model):
    link_name = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.link_name


class Comment(models.Model):
    post = models.ForeignKey('home_app.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, blank=True, null=True,  on_delete=models.CASCADE)
    content = models.TextField(verbose_name='Rəy')
    created_date = models.DateTimeField(auto_now_add=True)

