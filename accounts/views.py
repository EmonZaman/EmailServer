from urllib import request

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView as AuthLoginView, PasswordResetConfirmView, PasswordResetView
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url, redirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.utils.http import urlsafe_base64_decode
from django.views import View
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import CreateView, FormView
from django.views.generic import TemplateView
from environ import ImproperlyConfigured
from requests import get
from rest_framework.exceptions import ValidationError


from accounts.models import User


class AboutView(TemplateView):
    template_name = "accounts/index.html"

class BaseView(TemplateView):
    template_name = "accounts/base.html"


# noinspection PyMethodMayBeStatic
class LoginView(View):
    template_name = "accounts/login.html"
    template_index = "accounts/index.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        print(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        user = self.get_user(email, password)
        if user:
            login(request, user)
            return render(request, self.template_index)
        return render(request, self.template_name)

    def get_user(self, email, password):
        try:
            user = User.objects.get(email=email)
            print(user)
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user

        return None


class RegistrationView(View):
    template_name = "accounts/register.html"
    template_index = "accounts/index.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        print(request.POST)
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('password_confirm')
        print(username, email, password, confirm_password)
        # u = User()
        # u.objects.get(username=username)
        # u.objects.get(email=email)
        # u.objects.get(password=password)
        u = User.objects.create_user(username=username, email=email, password=password)
        u.set_password(password)
        u.save()
        login(request, u)
        return render(request, self.template_index)

    # model = User
    # form_class = UserForm
    # template_name = "accounts/registration.html"

class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)

        return redirect("accounts:login")
