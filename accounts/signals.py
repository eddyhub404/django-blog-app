from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings


from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings


@receiver(post_save, sender=User)
def send_welcome_mail(sender, instance, created, **kwargs):

    if created:

        html_content = render_to_string(
            'emails/welcome_email.html',
            {'user': instance}
        )

        email = EmailMultiAlternatives(
            subject='Welcome to EddyBlog 🎉',
            body='Welcome to EddyBlog',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[instance.email],
        )

        email.attach_alternative(html_content, "text/html")
        email.send()