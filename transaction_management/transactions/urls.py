# transactions/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionViewSet
from rest_framework.authtoken import views as drf_views
from . import views

router = DefaultRouter()
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('api/', include(router.urls)), 
    path('api-token-auth/', drf_views.obtain_auth_token), 
    path('', views.home, name='home'),
]
