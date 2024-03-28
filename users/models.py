from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser


class Gender(models.TextChoices):
    MALE = "M", "Male"
    FEMALE = "F", "Female"


class Identity(models.TextChoices):
    READER = "READER"
    AUTHOR = "AUTHOR"
    PUBLISHER = "PUBLISHER"


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=255, blank=True)
    # city = models.CharField(max_length=255, blank=True)
    # state = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    identity = models.CharField(max_length=55, choices=Identity)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    date_joined = models.DateTimeField(default=timezone.now)

    # specific fields for reader and author
    birth_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=55, choices=Gender, blank=True)

    # specific fields for publisher
    phone = models.CharField(max_length=20, blank=True)
    address = models.OneToOneField(
        Address, on_delete=models.CASCADE, blank=True, null=True
    )
    username = None

    # django depend on username in authentication process but
    # we want to depend on email in authentication process
    # because email is unique field
    # so we have to manually set username field to email
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
