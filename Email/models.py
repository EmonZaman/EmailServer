from django.db import models
from django.utils.translation import gettext as _

from accounts.models import User


class Mail(models.Model):
    sender_user = models.ForeignKey(
        User,
        related_name="sent_mail",
        on_delete=models.CASCADE,
    )
    sending_to = models.EmailField(max_length=254, null=True, blank=True)
    subject = models.CharField(max_length=250, null=True, blank=True)
    message = models.CharField(max_length=1000)

    sent = models.BooleanField(default=False)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE,  related_name="received_mail"
                                 , verbose_name=_("Receiver"))
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Email"
        verbose_name_plural = "Emails"

    def __str__(self):
        return f"{self.sender_user}-{self.receiver}-{self.subject}"
