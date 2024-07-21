from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny, DjangoModelPermissions

from .models import Product
from .serializers import ProductSerializer
from .permissions import MyCustomPermissionClass

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
	permission_classes = [MyCustomPermissionClass]
 
	# def get(self, request, format=None):
	# 	content = {
	# 		'user': str(request.user),  # `django.contrib.auth.User` instance.
	# 		'auth': str(request.auth),  # None
	# 	}
	# 	return Response(content)

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	permission_classes = [MyCustomPermissionClass]

