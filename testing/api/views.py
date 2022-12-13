from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response
from PIL import Image

from .serializers import ProductSerializer, ProductCreateSerializer
from .models import Product


def convert(image):
    im = Image.open(image).convert('RGB')
    im.save(f'media/images/{image.name}.webp', 'webp', optimize = True, quality = 10)
    return im


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    http_method_names = ['get', 'post']
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('status',)
    search_fields = ('name', 'vendor_code')

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return ProductSerializer
        return ProductCreateSerializer


    def create(self, request, *args):
        serializer = ProductCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        convert(request.data['image'])

