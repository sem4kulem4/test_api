from rest_framework import serializers
from PIL import Image

from .models import Product

def convert(image):
    im = Image.open(image).convert('RGB')
    im.save(f'img.webp', 'webp', optimize = True, quality = 10)
    print(im)
    return im



class ImageSerializer(serializers.Serializer):
    path = serializers.SerializerMethodField()
    format = serializers.SerializerMethodField()

    def get_path(self, obj):
        print(obj)
        path = ...
        return obj.path

    def get_format(self, obj):
        print(obj)
        formats = ...
        # return obj.name


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


    # def create(self, validated_data):
    #     print(validated_data)
    #     image = convert(validated_data['image'])
    #     validated_data['image'] = image
    #     print(validated_data)
    #     return Product.objects.create(**validated_data)

