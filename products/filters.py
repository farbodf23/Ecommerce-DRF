# products/filters.py
import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    # Price range
    min_price = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='gte',
        label='Minimum price'
    )
    max_price = django_filters.NumberFilter(
        field_name='price',
        lookup_expr='lte',
        label='Maximum price'
    )

    # Availability: stock > 0 means available
    in_stock = django_filters.BooleanFilter(
        method='filter_in_stock',
        label='In stock'
    )

    class Meta:
        model = Product
        fields = ['category']  # extra exact filters (optional)

    def filter_in_stock(self, queryset, name, value):
        """
        Filter products by availability.
        - ?in_stock=true → products with stock > 0
        - ?in_stock=false → products with stock = 0
        """
        if value is True:
            return queryset.filter(stock__gt=0)
        elif value is False:
            return queryset.filter(stock=0)
        return queryset
