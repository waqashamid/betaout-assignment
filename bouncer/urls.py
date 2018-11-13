from django.conf.urls import url
from .api import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^send/emails', SendEmail.as_view(), name='send_emails'),
    url(r'^user/data/(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})', UserEmailData.as_view(), name='get_user_data'),
]
