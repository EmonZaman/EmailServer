from django.urls import path
from .views import  UserView

app_name = "accounts-api-v1"

urlpatterns = [
    path('demo/',UserView.as_view(),name="Demo"),
]