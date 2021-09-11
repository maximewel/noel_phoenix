from django.contrib import admin
from phoenixapp.models import Gift, Address
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Gift)
admin.site.register(Address)
admin.site.register(User)