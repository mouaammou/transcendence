from rest_framework import generics, status
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

class ProductCreateAPIView(generics.CreateAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

	def create(self, request, *args, **kwargs):
		super().create(request, *args, **kwargs)
		return Response({"good, is created":"top"}, status=201)

	def perform_create(self, serializer):
		print(f"serialiaer data {serializer.validated_data}")
		title = serializer.validated_data.get("title")
		content = serializer.validated_data.get("content") or None
		if content is None:
			content = title
		serializer.save(content=content)