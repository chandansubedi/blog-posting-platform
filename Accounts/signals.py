from django.contrib.auth.models import User
from .models import AccountModel
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save , sender=User)
def create_profile(sender ,created, instance, *args, **kwargs):
    if created:
        AccountModel.objects.create(user=instance)