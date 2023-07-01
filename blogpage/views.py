from django.shortcuts import render
from .models import Article
# Create your views here.

def blogpage(request):
    articles=Article.objects.all()
    return render(request,'blogpage.html', context={'articles': articles})

def blogdetail(request,id):
    article=Article.objects.get(id=id)
    return render(request,'blogdetail.html',context={'article': article})   

def example(request):
    users=[
        {'name':'orxan','age':27,'job':'Software Developer'},
        {'name':'eli','age':24,'job':'Software Developer'},
        {'name':'aysel','age':21,'job':'Software Developer'},
        {'name':'senan','age':23,'job':'Software Developer'},
    ]
    return render(request,'example.html',context={'users':users})