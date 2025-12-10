from rest_framework.routers import DefaultRouter
from .views import EventViewSet, RSVPViewSet, ReviewViewSet

router = DefaultRouter()
router.register('events', EventViewSet)
router.register('rsvp', RSVPViewSet)
router.register('reviews', ReviewViewSet)

urlpatterns = router.urls
