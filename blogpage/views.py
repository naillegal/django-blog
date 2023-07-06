from django.shortcuts import render
from .models import Article,Author,Tag
# Create your views here.

def blogpage(request):
    author_username=request.GET.get('author')
    authors=Author.objects.all()
    articles=Article.objects.all()
    tags=Tag.objects.all()
    tag_title=request.GET.get('tag')
    if author_username:  
        articles=articles.filter(author__user__username=author_username)
    if tag_title:
        articles=articles.filter(tags__title=tag_title)
    return render(request,'blogpage.html', context={'articles': articles,'authors':authors,'tags':tags})     

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