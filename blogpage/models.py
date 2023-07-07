from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Author(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.CharField(max_length=25)

    def __str__(self):
        return self.user.username
    

class Tag(models.Model):
    title=models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Article(models.Model):
    title=models.CharField(max_length=20)
    description=models.TextField()
    content=models.TextField()
    show=models.BooleanField(default=True)
    view_count=models.IntegerField(default=0)
    image=models.ImageField(null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(Author,on_delete=models.SET_NULL,blank=True,null=True)
    tags=models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

