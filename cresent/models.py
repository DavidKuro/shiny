from django.db import models

# Create your models here.

class Description(models.Model):
    name=models.TextField(
        null=False,
        blank=False,
        max_length=20,
        unique=True,
    )

Destination=models.TextField(
    null=False,
    blank=False,
    max_length=20,
)

class product(models.Model):
    phone=models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=20,
    )
    name=models.CharField(
         null=False,
        blank=False,
        unique=True,
        max_length=20,
    )
    price=models.IntegerField(
        null=False,
        blank=False,
    )

class     