from django.db import models

# Create your models here.


class Article(models.Model):
    title=models.CharField(max_length=20)
    description=models.TextField()
    content=models.TextField()
    show=models.BooleanField(default=True)
    view_count=models.IntegerField()
    image=models.ImageField(null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

