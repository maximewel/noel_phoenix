from .serializers import *
from rest_framework import filters, permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response


class ViewsetFunctionPermissions(viewsets.ModelViewSet):
    """ 
    viewset thet allows to determine permissions by function :
        * Define permision_classes = [] as default permissions
        * Define permission_classes_by_action = { 'fct' : [permission], ... } as permission tailored for actions
    """
    class Meta:
        abstract = True

    def get_permissions(self):
        """Function that allow for defining permissions by function"""
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [AllowAny]
    permission_classes_by_action = {
        'create': [AllowAny],  # allow anyone to register
    }