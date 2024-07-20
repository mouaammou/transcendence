from django.urls import path

from . import views

urlpatterns = [
	path("products", views.ProductListCreateAPIView.as_view(), name="list products"),
	path("products/<int:pk>/create", views.ProductListCreateAPIView.as_view(), name="create a new product"),
	# path("products/<int:pk>/update", views.ProductUpdateAPIView.as_view(), name="update product"),
	# path("products/<int:pk>/delete", views.ProductDeleteAPIView.as_view(), name="Delete product"),
	# path("products/<int:pk>/detail", views.ProductDetailAPIView.as_view(), name="Detail product")
	path("products/<int:pk>", views.ProductRetrieveUpdateDestroyAPIView.as_view(), name="Detail product")
]
