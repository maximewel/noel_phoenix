from .viewsets import UserViewset
from rest_framework import routers 
  
router = routers.SimpleRouter() 

router.register(r'users', UserViewset, basename='users')