from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveUpdateAPIView
from .models import Profile, Cart
from .serializers import PublicProfileSerializer, OwnerProfileSerializer, CartSerializer
from .permissions import IsOwnerOrReadOnly, IsOwnerOnly
# Create your views here.
User = get_user_model()


class ProfileDetail(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self):
        username = self.kwargs['name']
        return get_object_or_404(Profile, user__username=username)

    def get_serializer_class(self):
        """
        - Owner gets the full serializer (for both read and write).
        - Everyone else gets the public serializer.
        """
        profile = self.get_object()
        request = self.request

        # Check if the authenticated user is the owner
        if request.user == profile.user:
            return OwnerProfileSerializer
        return PublicProfileSerializer


class CartDetail(RetrieveUpdateAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    permission_classes = [IsOwnerOnly]

    def get_object(self):
        username = self.kwargs['name']
        return get_object_or_404(Cart, user__username=username)
