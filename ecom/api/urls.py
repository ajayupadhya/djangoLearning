
from django.urls import path, include

from rest_framework import views
from .views import home
urlpatterns = [
    path('', home, name="api.home"),
    path('category/', include('api.category.urls')),
    path('product/', include('api.product.urls')),
    path('users/', include('api.user.urls')),
    path('order/', include('api.order.urls')),
    path('payment/', include('api.payment.urls')),
    # path('api-token-auth/', views.obtain_auth_token_, name='api_token-auth')

]
