"""
Views for the user API
"""
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .serializers import UserSerializer, AuthTokenSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user."""
    try:
        serializer_class = AuthTokenSerializer
        renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    except Exception as e:
        print(f'Fuck', e)


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    # How do you know that the user is the user they say they are
    permission_classes = [permissions.IsAuthenticated]

    # we know who the user is Now what is he allowed to do with the system

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user  # retrieving the user that is attached with the request

