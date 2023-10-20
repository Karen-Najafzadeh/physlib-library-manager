from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('librarians', views.LibrarianViewSet)
router.register('shifts', views.ShiftViewSet)

urlpatterns = [
    path('',include(router.urls))
]
