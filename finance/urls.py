from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('treasury', views.TreasuryViewSet)

urlpatterns = [
    path('', include(router.urls))
]
