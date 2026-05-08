# users/serializers.py
from .models import Cart, CartItem
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()


class UserBasicSerializer(serializers.ModelSerializer):
    """Minimal user info shown in public profile."""
    class Meta:
        model = User
        fields = ['id', 'username']
        read_only_fields = fields


class PublicProfileSerializer(serializers.ModelSerializer):
    """
    What non-owners see: only username and avatar.
    """
    user = UserBasicSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['user', 'avatar',]


class OwnerProfileSerializer(serializers.ModelSerializer):
    """
    What the owner sees: all fields including sensitive info.
    """
    user = UserBasicSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = [
            'user',
            'phone',
            'address',
            'city',
            'postal_code',
            'avatar',

        ]


# users/serializers.py


class CartItemSerializer(serializers.ModelSerializer):
    """Shows product details inside the cart."""
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_price = serializers.DecimalField(
        source='product.price', max_digits=10, decimal_places=2, read_only=True)
    line_total = serializers.DecimalField(
        read_only=True, max_digits=10, decimal_places=2)

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_name',
                  'product_price', 'quantity', 'line_total']


class CartSerializer(serializers.ModelSerializer):
    """Cart with its items and computed totals."""
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.DecimalField(
        read_only=True, max_digits=10, decimal_places=2)
    total_items = serializers.IntegerField(read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'total_items',
                  'total_price', 'updated_at']
        read_only_fields = ['user', 'updated_at']
