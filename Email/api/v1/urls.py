from .views import MailView, MailDetail, DraftView, UserInboxListView, UserSentListView
from django.urls import path
app_name = "Email-api-v1"



urlpatterns = [
    path('',MailView.as_view(),name="mail"),
    path('detail/<pk>/', MailDetail.as_view(), name="maildetail"),
    path('draft/', DraftView.as_view(), name="Draft"),
    path('userinbox/', UserInboxListView.as_view(), name="inbox"),
    path('usersentitems/', UserSentListView.as_view(), name="sent"),

]


