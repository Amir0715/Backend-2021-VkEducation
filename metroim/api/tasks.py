from celery import shared_task
from django.core.mail import EmailMessage
from datetime import datetime
from django.contrib.auth import get_user_model
from django.conf import settings


@shared_task
def save_user_count():
    User = get_user_model()
    user_count = User.objects.count()
    debug_str = "[{}] User count = {}\n".format(datetime.now().isoformat(), user_count)
    with open('users_count.log', mode='a') as f:
        f.write(debug_str)
    return user_count


@shared_task
def send_email(subject, text, sender=None, recipient=None):
    if recipient is None:
        recipient = settings.ADMINS
        if not recipient:
            raise Exception('Email recipients is empty1')
    message = EmailMessage(
        subject,
        text,
        from_email=sender,
        to=recipient)
    return message.send()
