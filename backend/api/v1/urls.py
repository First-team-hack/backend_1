from django.urls import path, include
from . import views

urlpatterns = [
    path('events', views.EventsView.as_view()),
    path('events/completed', views.CompletedEventsView.as_view()),
    path('profile/users/me', views.UserView.as_view()),
    path('profile/events/registered', views.RegisteredEventsView.as_view()),
    path('profile/events/favorites', views.FavoritesEventsView.as_view()),
    path('profile/events/recommended', views.RecommendedEventsView.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
