from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    profile_picture = models.ImageField(
        upload_to='profile_pictures',
        blank=True,
        null=True,
        help_text='Upload a profile picture (optional)',
        verbose_name='Profile Picture'
    )

    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^(\+359|0)?8[789]\d{7}$',
                message='Please correct valid phone number'
            )
        ],
        help_text='089999999',
    )

    def __str__(self):
        return f'{self.user.username} Profile'

