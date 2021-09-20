from django.urls import path, reverse_lazy
from accounts.views import LoginView, RegistrationView, AboutView, LogoutView, BaseView

app_name = "accounts"





urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegistrationView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    # path("logout/", LogoutView.as_view(next_page=reverse_lazy("accounts:login")), name="logout"),
    path('', AboutView.as_view(), name="index"),
    path("base/", BaseView.as_view(), name="base"),

 ]