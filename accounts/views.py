from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class BaseView(TemplateView):
    template_name = "accounts/base.html"

class RegisterView(TemplateView):
        template_name = "accounts/login.html"