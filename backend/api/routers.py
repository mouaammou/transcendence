from rest_framework.routers import DefaultRouter
from .viewsets import ProductGereralViewSets

router = DefaultRouter()

router.register('all-products', ProductGereralViewSets, basename='generic viewsets')
urlpatterns = router.urls