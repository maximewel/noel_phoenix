from rest_framework import serializers
from phoenixapp.models import Gift, Address
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class AdressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('__all__')

class GiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gift
        fields = ('__all__')