from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()

router.register('profile/users', views.UserViewSet)
router.register(r'profile/(?P<user_id>\d+)/events',
                views.UserEventsViewSet, basename='user_event')
router.register('profile/events', views.EventsViewSet)
router.register('profile/useractivities', views.UserActivitiesViewSet)

urlpatterns = [
    path('', include(router.urls), name='profile'),
]
