from .viewsets import UserViewset, GiftViewset
from rest_framework import routers 
  
router = routers.SimpleRouter() 

router.register(r'users', UserViewset, basename='users')
router.register(r'gifts', GiftViewset, basename='users')