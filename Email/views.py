from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView

import Email
from Email.models import Mail


class ComposeView(View):
    template_name = "Email/compose.html"
    template_index = "accounts/base.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        print(request.POST)
        sending_mail = request.POST.get('email')
        subject= request.POST.get('subject')
        message = request.POST.get('message')

        print(sending_mail,subject,message)
        # u = User()
        # u.objects.get(username=username)
        # u.objects.get(email=email)
        # u.objects.get(password=password)
        u = Mail.objects.get(sending_to=sending_mail, subject=subject, message=message)

        u.save()
        # login(request, u)
        return render(request, self.template_index)

    # model = User
    # form_class = UserForm
    # template_name = "accounts/registration.html"

