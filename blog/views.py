from django.shortcuts import render
from django.views.generic import ListView
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


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "blog/home.html", context)


class PostListView(ListView):
    model = Post


def about(request):
    return render(request, "blog/about.html", {'title': 'About'})
