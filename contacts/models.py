from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone


class Person(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=250)
    phone = PhoneNumberField()

    def __str__(self):
        return self.name
