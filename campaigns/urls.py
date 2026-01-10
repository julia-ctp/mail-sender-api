from .views import CampaignViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"", CampaignViewset, basename="campaigns")

urlpatterns = router.urls
