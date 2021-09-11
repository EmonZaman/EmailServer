from .views import MailView, MailDetail
from django.urls import path
app_name = "Email-api"



urlpatterns = [
    path('mail/',MailView.as_view(),name="mail"),
    path('mail/detail/<pk>/', MailDetail.as_view(), name="maildetail"),
]