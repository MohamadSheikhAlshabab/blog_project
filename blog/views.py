from django.shortcuts import render
from .models import Post
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.

class HomePageView(ListView):
    template_name = 'home.html'
    model=Post

class BlogListView(ListView):
    template_name = 'list_blog.html'
    model=Post

class BlogDetailView(DetailView):
    template_name = 'post_detail.html'
    model=Post
