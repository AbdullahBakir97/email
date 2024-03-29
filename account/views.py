from django.shortcuts import render, redirect
from django.contrib.auth import login 
from .forms import RegistrationForm
from allauth.account.views import (
    PasswordChangeView,
    PasswordResetDoneView,
    PasswordResetView,
    LoginView,
    LogoutView,
    SignupView,
)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            login(request, user)
            return redirect('base')
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})





def custom_signup(request):
    # Your custom signup logic here
    return render(request, 'account/custom_signup.html', {})

class PasswordChangeView(PasswordChangeView):
    template_name = 'password/change.html'

class PasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password/reset_done.html'

class PasswordResetView(PasswordResetView):
    template_name = 'password/reset.html'

class LoginView(LoginView):
    template_name = 'account/login.html'

class LogoutView(LogoutView):
    template_name = 'account/logout.html'

class SignupView(SignupView):
    template_name = 'registration/signup.html'
