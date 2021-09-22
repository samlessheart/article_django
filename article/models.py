from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    link = models.CharField(max_length=400)
    author = models.ForeignKey(User, on_delete=models.SET('no author'))

    @property
    def small_content(self):
        return self.content[0:100] + " ..."
    
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=150)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    
    

    
    