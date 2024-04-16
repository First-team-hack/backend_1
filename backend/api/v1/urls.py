from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()

# router.register('profile/events', views.UserEventsViewSet,
#                 basename='user_events')
# router.register('events', views.EventsViewSet)


router.register('profile/useractivities', views.UserActivitiesViewSet)
router.register('profile/userfavorites', views.UserFavoritesViewSet)


urlpatterns = [
    path('', include(router.urls), name='profile'),
    path('profile/users/me', views.UserView.as_view()),
    path('events', views.EventsView.as_view()),
    path('events/completed', views.CompletedEventsView.as_view()),
    path('profile/events/registered', views.RegisteredEventsView.as_view()),
    path('profile/events/favorites', views.FavoritesEventsView.as_view()),
    path('profile/events/recommended', views.RecommendedEventsView.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
