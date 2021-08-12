from django.db import models

# Create your models here.


class AddUser(models.Model):
    firstName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    phoneNumber = models.BigIntegerField(unique=True)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.email
