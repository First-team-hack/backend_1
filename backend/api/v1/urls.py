from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()

router.register('profile/users', views.UserViewSet)
router.register('profile/events', views.UserEventsViewSet,
                basename='user_events')
router.register('profile/events/completed',
                views.UserEventsViewSet, basename='user_completed_events')
router.register('profile/useractivities', views.UserActivitiesViewSet)


urlpatterns = [
    path('', include(router.urls), name='profile'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
