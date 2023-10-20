from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('treasury', views.TreasuryViewSet)
router.register('income', views.IncomeViewSet)
router.register('expense', views.ExpenseViewSet)

urlpatterns = [
    path('', include(router.urls))
]
