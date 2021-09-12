from .views import MailView, MailDetail, DraftView, UserInboxListView, UserSentListView
from django.urls import path
app_name = "Email-api"



urlpatterns = [
    path('',MailView.as_view(),name="mail"),
    path('detail/<pk>/', MailDetail.as_view(), name="maildetail"),
    path('draft/', DraftView.as_view(), name="Draft"),
    path('userinboxlist/', UserInboxListView.as_view(), name="userlist"),
    path('usersentlist/', UserSentListView.as_view(), name="userlist"),

]




