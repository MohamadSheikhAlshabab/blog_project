from .views import HomePageView,BlogListView,BlogDetailView
from django.urls import path

urlpatterns = [
    path('',HomePageView.as_view(),name = 'blog_home'),
    path('list/',BlogListView.as_view(),name = 'blog_list'),
    path('blog/<int:pk>',BlogDetailView.as_view(),name = 'blog_detail'),
]
