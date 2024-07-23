from products.models import Product
from rest_framework.viewsets import ModelViewSet
from products.serializers import ProductSerializer

class ProductGereralViewSets(ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer