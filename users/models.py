from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from datetime import timedelta


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True)

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expiers = models.DateTimeField(default=(now() + timedelta(hours=48)))

    def safe_delete(self):
        self.is_active = False
        self.save()

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expiers:
            return False
        else:
            return True
