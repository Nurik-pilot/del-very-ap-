from rest_framework.routers import DefaultRouter
from .views import DeliveryOrderViewSet

router = DefaultRouter()
router.register(r'orders', DeliveryOrderViewSet, basename='orders')

urlpatterns = router.urls
