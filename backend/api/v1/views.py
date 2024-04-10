from rest_framework import viewsets
from users.models import User, UserActivities
from events.models import Event
from . import serializers
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """Простой вьюсет для пользователя."""
    queryset = User.objects.all()
    serializer_class = serializers.UserUpdateSerializer


# Пока сделан только чтоб в базу данные закидывать
class EventsViewSet(viewsets.ModelViewSet):
    """Простой вьюсет для мероприятия."""
    queryset = Event.objects.all()
    serializer_class = serializers.EventSerializer


class UserEventsViewSet(viewsets.ViewSet):
    """Вьюсет мероприятий пользователя"""
    def list(self, request, user_id):
        user_activities = UserActivities.objects.filter(
            user=user_id).values('event')

        events_queryset = Event.objects.filter(pk__in=user_activities)
        serializer = serializers.EventSerializer(events_queryset, many=True)

        events_data = serializer.data

        response_data = {
            "success": True,
            "code": 200,
            "events": events_data
        }

        return Response(response_data)


# Пока сделан только чтоб в базу данные закидывать
class UserActivitiesViewSet(viewsets.ModelViewSet):
    """Вьюсет для записей в UserActivities."""
    queryset = UserActivities.objects.all()
    serializer_class = serializers.UserActivitiesSerializer
