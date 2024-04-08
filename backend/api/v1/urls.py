from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()

router.register('profile/users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls), name='profile'),
]
