from rest_framework import serializers

from Email.models import Mail


class MailSerailizers(serializers.ModelSerializer):


    class Meta:
        model = Mail
        fields = ['user', 'sending_to', 'subject',  'message', 'date','sent']