from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Gift(models.Model):
    """ The gift is a relationship between two users with a status (sent, received)"""
    sender = models.ForeignKey(User)
    recipient = models.ForeignKey(User)
    sent = models.BooleanField()
    received = models.BooleanField()

    def __str__(self):
        return f"{self.sender} to {self.recipient}"