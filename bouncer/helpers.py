from betaout.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

def send_email(email, body, subject):

    from_email = EMAIL_HOST_USER
    to_list = email
    message = body
    try:
        send_mail(subject, message, from_email, to_list, fail_silently=True)
    except KeyError as e:
        return 3, str(e)
    return 0, "Mails sent"