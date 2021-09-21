from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import TemplateView, DetailView
from django.views.generic.list import ListView
import Email
from Email.models import Mail
from accounts.models import User


class ComposeView(View):
    template_name = "Email/compose.html"
    template_index = "accounts/base.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        print(request.POST)
        sender_user = request.user
        sending_mail = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        print(sending_mail, subject, message, sender_user)

        u = Mail()
        u.sender_user = sender_user
        u.sending_to = sending_mail
        u.subject = subject
        u.message = message

        u.save()
        # login(request, u)
        return redirect('Email:inbox')

    # model = User
    # form_class = UserForm
    # template_name = "accounts/registration.html"


class Inbox(ListView):
    template_name = "Email/inbox.html"
    context_object_name = "Mails"

    def get_queryset(self):
        return Mail.objects.filter(Q(receiver__id=self.request.user.id) | Q(sender_user__id=self.request.user.id))


class Sent(ListView):
    template_name = "Email/sentitems.html"
    context_object_name = "Mails"

    def get_queryset(self):
        return Mail.objects.filter(Q(sender_user__id=self.request.user.id))


class DetailView(DetailView):
    template_name = "Email/details.html"
    model= Mail


class SentDetail(DetailView):
    template_name = "Email/senderdetail.html"
    model= Mail

