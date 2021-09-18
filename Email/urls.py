from django.urls import path
from Email.views import ComposeView, ListView, Inbox, Sent

app_name = "Email"

urlpatterns = [

    path("compose/", ComposeView.as_view(), name="compose"),
    path("inbox/", Inbox.as_view(), name="inbox"),
    path("sent/", Sent.as_view(), name="sent"),

]


