from rest_framework import serializers

from Email.models import Mail


class MailSerailizers(serializers.ModelSerializer):


    class Meta:
        model = Mail
        fields = ['sender_user', 'sending_to', 'subject',  'message', 'sent','receiver', 'created_date', 'modified_date']