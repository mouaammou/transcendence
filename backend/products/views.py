from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Product
from .serializers import ProductSerializer

# class ProductCreateAPIView(generics.CreateAPIView): #crearte, get
# 	queryset = Product.objects.all()
# 	serializer_class = ProductSerializer

# class ProductUpdateAPIView(generics.UpdateAPIView): #update, post, put
# 	queryset = Product.objects.all()
# 	serializer_class = ProductSerializer

# class ProductDetailAPIView(generics.RetrieveAPIView): #read, get
# 	queryset = Product.objects.all()
# 	serializer_class = ProductSerializer

# class ProductDeleteAPIView(generics.DestroyAPIView): #delete
# 	queryset = Product.objects.all()
# 	serializer_class = ProductSerializer

# class ProductListAPIView(generics.ListAPIView): #list all products
# 	queryset = Product.objects.all()
# 	serializer_class = ProductSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	permission_classes = [AllowAny]

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

