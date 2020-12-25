from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
)
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/write/', PostCreateView.as_view(), name='post-write'),
    path('post/<int:pk>/edit', PostUpdateView.as_view(), name='post-edit'),
    path('about/', views.about, name='blog-about'),
]
