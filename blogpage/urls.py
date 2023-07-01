from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('blogpage/',views.blogpage,name='blogpage'),
    path('blogpage/<int:id>/',views.blogdetail,name='blogdetail'),
    path('example/',views.example),
]