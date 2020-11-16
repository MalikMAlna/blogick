from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .forms import (RegistrationForm,
                    # LoginForm
                    )


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
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(
                username=username,
                password=raw_password
            )
            login(request, account)
            return HttpResponseRedirect(
                request.GET.get('next', reverse('blog-home'))
            )
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, html, context)
