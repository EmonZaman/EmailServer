from django.urls import path
from .views import UserView

app_name = "accounts-api-v1"

urlpatterns = [
    path('register/',UserView.as_view(),name="register"),

]
