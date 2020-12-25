from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# posts_stub = [
#     {
#         'author': 'Mike A.',
#         'title': 'First Blog Post',
#         'content': 'blah blah blah blah',
#         'date_posted': 'May 24, 2020'
#     },
#     {
#         'author': 'Hakim D.',
#         'title': 'Blog Post 2',
#         'content': 'blah blah blah blah',
#         'date_posted': 'May 24, 2020'
#     }
# ]

# Function View Example for Home
# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, "blog/home.html", context)


class PostListView(ListView):
    model = Post
    # Default template_name is <app_name>/<model_name>_<viewtype>.html
    template_name = 'blog/home.html'
    # Now setting context, default context_object_name is object_list
    # for ListView
    context_object_name = 'posts'
    # Newest to oldest by date posted
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


def about(request):
    return render(request, "blog/about.html", {'title': 'About'})
