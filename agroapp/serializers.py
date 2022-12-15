from .models import *
from rest_framework import serializers
                  
class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = ('PRODUCT_NAME',
                  'PRODUCT_DESCRIPTION',
                  'CATEGORY',
                  'PRICE',
                  'QUANTITY',
                  'IMAGE',
                  'STATUS')