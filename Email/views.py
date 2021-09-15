from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class ComposeView(TemplateView):
    template_name = 'Email/compose.html'
