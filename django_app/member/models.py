from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.crypto import get_random_string


class MyUserManager(UserManager):
    def create_facebook_user(self, social_id, user_type, email=None, password=None, **extra_fields):
        extra_username = get_random_string(10)
        return super().create_user(
            username='{}{}'.format(social_id, extra_username),
            social_id=social_id,
            user_type=user_type,
            email=email,
            password=password,
            **extra_fields
        )


class MyUser(AbstractUser):
    CHOICES_USER_TYPE = (
        ('django', 'Django'),
        ('facebook', 'Facebook'),
    )
    user_type = models.CharField(
        max_length=15,
        choices=CHOICES_USER_TYPE,
        default=CHOICES_USER_TYPE[0][0]
    )
