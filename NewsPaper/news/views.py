# from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from .models import Post

 
class NewsList(ListView):
    model = Post  
    template_name = 'news.html'  
    context_object_name = 'news'
    queryset = Post.objects.filter(post_type='NW').order_by('-id')  
    

class NewsDetail(DetailView):
    model = Post 
    template_name = 'newsDetail.html' 
    context_object_name = 'newsDetail' 
    queryset = Post.objects.filter(post_type='NW')

