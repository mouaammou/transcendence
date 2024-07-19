from django.urls import path

from . import views

urlpatterns = [
	path("", views.ProductCreateAPIView.as_view(), name="product create"),
	path("<int:pk>", views.ProductDetailAPIView.as_view(), name="productAPIView")
]
