from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse

class ProductSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = ['user','url', 'id', 'title', 'price', 'sale_price', 'get_discount']  
    
    def get_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-detail", kwargs={"pk": obj.pk}, request=request)
    
    def validate_title(self, value):
        qs = Product.objects.filter(title__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} is already a product name")
        return value
    
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price must be greater than zero")
        return value