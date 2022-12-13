from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from PIL import Image

from .serializers import ProductSerializer, ProductCreateSerializer
from .models import Product

def convert(image):
    im = Image.open(image).convert('RGB')
    im.save(f'{image}.webp', 'webp', optimize = True, quality = 10)
    print(im)
    return im

# class ProductViewSet(ViewSet):
#     def create(self, data):
#         pass
#     def perform_create(self, serializer):
#         print(serializer)
#
#
#     def list(self, request):
#         queryset = Product.objects.all()
#         serializer = ProductSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         item = get_object_or_404(Product, pk=pk)
#         serializer = ProductSerializer(item)
#         return Response(serializer.data)

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    http_method_names = ('get', 'post')

    def get_serializer_class(self):
        if self.action in ('retrieve', 'list'):
            return ProductSerializer
        return ProductCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = ProductCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        image = convert(request.data['image'])
        return Response(serializer.data)
