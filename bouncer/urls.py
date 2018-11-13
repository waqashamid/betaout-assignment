from django.conf.urls import url
from .api import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^send/emails', SendEmail.as_view(), name='send_emails'),
]
