from django.urls import path, include

from rest_framework.routers import DefaultRouter

from disaster_app.views import DisasterViewset

router = DefaultRouter()
router.register("data", DisasterViewset, basename="disaster-data")

urlpatterns = [
    path('', include(router.urls))
]