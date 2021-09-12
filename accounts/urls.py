from django.urls import path
from accounts.views import BaseView, RegisterView

app_name = "accounts"

urlpatterns = [
    path("base/", BaseView.as_view(), name="base"),
    path("register/", RegisterView.as_view(), name="register"),

 ]