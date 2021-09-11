from .views import MailView, MailDetail, DraftView
from django.urls import path
app_name = "Email-api"



urlpatterns = [
    path('mail/',MailView.as_view(),name="mail"),
    path('mail/detail/<pk>/', MailDetail.as_view(), name="maildetail"),
    path('mail/draft/', DraftView.as_view(), name="Draft"),
    # path('mail/usermaillist/', UserEmailListView.as_view(), name="userlist"),

]

