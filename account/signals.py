from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import EmailAccount

User = get_user_model()

@receiver(post_save, sender=User)
def create_email_account(sender, instance, created, **kwargs):
    if created:
        # Ensure that the user doesn't already have an associated email account
        if not hasattr(instance, 'emailaccount'):
            # You can implement email account creation logic here
            # For simplicity, we'll create a local EmailAccount record
            EmailAccount.objects.create(user=instance, email_address=instance.email, password=instance.password)
