from products.models import Product
from django_filters import rest_framework as filters

class ProductFilter(filters.FilterSet):
    category = filters.CharFilter(lookup_expr="icontains")
    name = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Product
        fields = ["category", "name"]
        