from django.urls import path, include
from rest_framework import routers
from rest_framework_nested import routers as nested_routers
from . import views

router = routers.DefaultRouter()
router.register('books', views.BookViewset)
router.register('members', views.MemberViewset)
router.register('lockers', views.LockerViewset)

n_router = nested_routers.NestedDefaultRouter(router, 'lockers', lookup = 'locker')
n_router.register('booking', views.Booking)

income_nested_router = nested_routers.NestedDefaultRouter(n_router, 'booking', lookup='new_income')
income_nested_router.register('pricing', views.Pricing)
urlpatterns = [
    path('', include(router.urls)),
    path('',include(n_router.urls)),
    path('',include(income_nested_router.urls)),
]
