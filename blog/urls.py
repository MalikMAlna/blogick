from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView
)
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/write/', PostCreateView.as_view(), name='post-write'),
    path('about/', views.about, name='blog-about'),

]
