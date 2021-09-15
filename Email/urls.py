from django.urls import path
from Email.views import ComposeView

app_name = "accounts"

urlpatterns = [

    path("compose/", ComposeView.as_view(), name="Compose"),

 ]


