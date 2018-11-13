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

        msg = send_email(emails, body, subject)
        if msg[0] == 0:
            return Response({"Success" : "Emails sent"}, status=status.HTTP_200_OK)