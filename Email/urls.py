from django.urls import path

from Email import views
from Email.views import ComposeView, ListView, Inbox, Sent, DetailView, SentDetail

app_name = "Email"

urlpatterns = [

    path("compose/", ComposeView.as_view(), name="compose"),
    path("inbox/", Inbox.as_view(), name="inbox"),
    path("inbox/<pk>/",DetailView.as_view(), name="detail"),
    path("sent/", Sent.as_view(), name="sent"),
    path("sent/<pk>", SentDetail.as_view(), name="sent"),

]


