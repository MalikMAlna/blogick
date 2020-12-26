from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
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
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'
    # Default context_object_name is object
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # Default template_name <app_name>/<model_name>_form.html
    template_name = 'blog/post-write.html'
    fields = ('title', 'content')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    # Default template_name <app_name>/<model_name>_form.html
    template_name = 'blog/post-write.html'
    fields = ('title', 'content')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post-delete-confirm.html'
    # Default context_object_name is object
    context_object_name = 'post'
    success_url = '/'

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, "blog/about.html", {'title': 'About'})
