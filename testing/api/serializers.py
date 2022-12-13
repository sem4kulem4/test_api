from rest_framework import serializers
from PIL import Image

from .models import Product


class ImageSerializer(serializers.Serializer):
    path = serializers.SerializerMethodField()
    format = serializers.SerializerMethodField()

    def get_path(self, obj):
        path = obj.name.split('.')[0]
        return 'media/' + path

    def get_format(self, obj):
        formats = obj.name.split('.')[1:]
        formats.append('webp')
        return formats


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField()
    vendor_code = serializers.CharField()
    price = serializers.IntegerField()
    status = serializers.CharField()
    image = ImageSerializer()


class ProductCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'name',
            'vendor_code',
            'price',
            'status',
            'image'
        )
