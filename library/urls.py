from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('books', views.BookViewset)
router.register('members', views.MemberViewset)

urlpatterns = [
    path('', include(router.urls))
]
