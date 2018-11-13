from django.shortcuts import render
from .models import *
from rest_framework import status, views
from rest_framework.response import Response
from .serializer import *
from django.db.utils import DatabaseError
from django.http import HttpResponse, StreamingHttpResponse
from .helpers import *

class SendEmail(views.APIView):

    def post(self, request, **kwargs):
        try:
            emails = request.data['emails']
            body = request.data['body']
            subject = request.data['subject']
        except KeyError as e:
            return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        email_data, created = EmailData.objects.get_or_create(body=body, subject=subject)
        for email in emails:
            user, created = User.objects.get_or_create(email=email)
            user.emails_received.add(email_data)
            user.save()
        msg = send_email(emails, body, subject)
        if msg[0] == 0:
            return Response({"Success" : "Emails sent"}, status=status.HTTP_200_OK)
        else:
            return Response({"Error": str(msg[0])}, status=status.HTTP_304_NOT_MODIFIED)

class UserEmailData(views.APIView):

    def get(self, request, **kwargs):
        try:
            email = kwargs.get('email')
        except KeyError as e:
            return Response({"Error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        print(email)
        user = User.objects.get(email=email)
        if user:
            return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
        else:
            return Response({"Error" : "User does not exist"}, status=status.HTTP_404_NOT_FOUND)