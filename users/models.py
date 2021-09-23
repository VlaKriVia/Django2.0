from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
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

class ShopUserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOISES = (
        (MALE, 'M'),
        (FEMALE, 'W')
    )


    users = models.OneToOneField(
        User,
        unique=True,
        null=False,
        db_index=True,
        on_delete=models.CASCADE
    )


    tagline = models.CharField(
        verbose_name="тэги",
        max_length=128,
        blank=True
    )


    aboutme = models.TextField(
        verbose_name="о себе",
        max_length=512,
        blank=True
    )


    gender = models.CharField(
        verbose_name='пол',
        max_length=1,
        choises=GENDER_CHOISES,
        blank=True
    )


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            ShopUserProfile.create(user=instance)


    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.shopuserprofile.save()
