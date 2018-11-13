from rest_framework import serializers
from . import models

class EmailDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.EmailData
        fields = ('id', 'subject', 'body', 'created', 'modified', )


class UserSerializer(serializers.ModelSerializer):
    emails_received = EmailDataSerializer(read_only=True, many=True)

    class Meta:
        model = models.User
        fields = ('id', 'email', 'emails_received', 'created', 'modified', )

