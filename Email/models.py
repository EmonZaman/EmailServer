from django.db import models

from accounts.models import User


class Mail(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    sending_to = models.EmailField(max_length=254, null=True, blank=True)
    subject = models.CharField(max_length=250, null=True, blank=True )
    message = models.CharField(max_length=1000)
    date = models.DateTimeField()
    sent= models.BooleanField(default=False)

