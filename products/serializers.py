from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(
        format='%Y/%m/%d',
        input_formats=['%Y/%m/%d', 'iso-8601'],   # accepts both
        required=True
    )

    class Meta:
        model = Category
        fields = ["name", "description", "created_at"]

    def validate_created_at(self, value):
        if value is None:
            raise serializers.ValidationError("Date cannot be null.")
        if value.year > 2025 or value.year < 2010:
            raise serializers.ValidationError(
                "Date must be between 2010 and 2025.")
        return value


class ProductSerializer(serializers.ModelSerializer):

    updated_at = serializers.DateTimeField(
        format='%Y/%m/%d',
        required=True)

    class Meta:
        model = Product
        fields = ["name", "description", "price",
                  "image", "stock", "updated_at"]
