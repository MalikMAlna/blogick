from django.shortcuts import render, reverse, HttpResponseRedirect
# from django.contrib.auth import authenticate, login
from .forms import (RegistrationForm,
                    AccountUpdateForm,
                    ProfileUpdateForm,
                    # LoginForm
                    )
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from .models import Profile
from blog.models import Post


# def register(request):
#     form = UserCreationForm()
#     return render(request, "authentication/register.html", {"form": form})

def register(request):
    html = 'authentication/register.html'
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            # ____ Auto-login on successful account creation _____

            # username = form.cleaned_data.get('username')
            # display_name = form.cleaned_data.get('display_name')
            # raw_password = form.cleaned_data.get('password1')
            # account = authenticate(
            #     username=username,
            #     password=raw_password
            # )
            # login(request, account)
            messages.success(
                request,
                # f"Account successfully created for {display_name}! " +
                "Please log in with your new account credentials."
            )
            return HttpResponseRedirect(
                request.GET.get('next', reverse('login'))
            )
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, html, {"form": form})


@login_required
def profile(request):
    html = 'authentication/profile.html'
    if request.method == 'POST':
        au_form = AccountUpdateForm(request.POST, instance=request.user)
        pu_form = ProfileUpdateForm(request.POST,
                                    request.FILES,
                                    instance=request.user.profile)
        if au_form.is_valid() and pu_form.is_valid():
            au_form.save()
            pu_form.save()
            messages.success(
                request,
                "Your account and profile info " +
                "have been successfully updated!"
            )
            return HttpResponseRedirect(
                request.GET.get('next', reverse('profile'))
            )
    else:
        au_form = AccountUpdateForm(instance=request.user)
        pu_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'au_form': au_form,
        'pu_form': pu_form
    }
    return render(request, html, context)


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'authentication/other-profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(
            *args, **kwargs)
        context["profile"] = self.get_object()
        context["account_post_count"] = Post.objects.filter(
            author=self.get_object().account).count()
        return context

# Custom Login/Logout Views

# def loginview(request):
#     html = 'login.html'
#     context = {}
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             user = authenticate(
#                 request,
#                 username=data['username'],
#                 password=data['password'],
#             )
#             if user:
#                 login(request, user)
#                 return HttpResponseRedirect(
#                     request.GET.get('next', reverse('homepage'))
#                 )
#         else:
#             context['login_form'] = form
#     else:
#         form = LoginForm()
#         context['login_form'] = form
#     return render(request, html, context)


# def logoutview(request):
#     logout(request)
#     messages.info(request, "Logged out successfully!")
#     return HttpResponseRedirect(reverse('homepage'))
