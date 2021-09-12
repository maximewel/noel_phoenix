from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Gift(models.Model):
    """ The gift is a relationship between two users with a status (sent, received)"""
    #Can't delete a user involved in a gift: the gift must be deleted first.
    sender = models.OneToOneField(User, on_delete=models.RESTRICT, related_name="giftOut")
    recipient = models.OneToOneField(User, on_delete=models.RESTRICT, related_name="giftIn")
    sent = models.BooleanField()
    received = models.BooleanField()

    def __str__(self):
        return f"{self.sender} to {self.recipient}"

class Address(models.Model):
    """ Holds the physical adress of a user"""
    #user
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #Informations
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    street = models.CharField(max_length=100)
    postalCode = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.username} address"