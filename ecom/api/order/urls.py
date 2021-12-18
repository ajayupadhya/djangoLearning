from rest_framework import routers
from django.urls import path, include


from . import views

router = routers.DefaultRouter()
# router.register(r'', views.OrderViewSet)

urlpatterns = [
    # path("", include(router.urls)),
    path("", views.OrderViewSet.as_view(),name="order_view_set"),
    path("add/<str:id>/", views.add,  name="order.add")
]
