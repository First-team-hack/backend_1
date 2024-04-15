from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response

from users.models import (User,
                          UserActivities,
                          SelectedEvents)
from events.models import Event, Favorite

from . import serializers
from .serializers import EventSerializer, FavoriteSerializer


class EventsViewSet(viewsets.ModelViewSet):

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    @action(
        detail=True,
        methods=['post', 'delete'],
        url_path='favorite',
        url_name='favorite',
        permission_classes=(permissions.IsAuthenticated,)
    )
    def get_favorite(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        if request.method == 'POST':
            serializer = FavoriteSerializer(
                data={'user': request.user.id, 'event': event.id}
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            favorite_serializer = FavoriteSerializer(event)
            return Response(
                favorite_serializer.data, status=status.HTTP_201_CREATED
            )
        favorite_event = get_object_or_404(
            Favorite, user=request.user, event=event
        )
        favorite_event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserView(APIView):
    """Вью для пользователя."""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = User.objects.get(id=request.user.id)

        serializer = serializers.UserSerializer(
            user, context=self.request)
        return Response(serializer.data)

    def patch(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = serializers.UserSerializer(
            user, data=request.data, partial=True, context=self.request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisteredEventsView(APIView):
    """Вью зарегистрированных ивентов пользователя."""
    permission_classes = [permissions.IsAuthenticated]
    queryset = UserActivities.objects.all()
    serializer_class = serializers.RegisteredEventSerializer

    def get(self, request):
        events_ids = UserActivities.objects.filter(
            user=request.user.id).values('event')
        events = None
        for event_id in events_ids:
            events = Event.objects.filter(id=event_id['event'])
        print(events)
        serialized_event = serializers.EventSerializer(events, many=True)
        return Response(
            serialized_event.data, status=status.HTTP_200_OK
        )

    def post(self, request):
        print('POSTsosal')
        data = request.data
        print(data)
        already_registered = UserActivities.objects.filter(
            user=request.user.id,
            event=data['event_id']
        )
        serializer = serializers.UserActivitiesSerializer(
            data={'user': request.user.id, 'event': data['event_id']}
        )
        if len(already_registered) > 0:
            event = get_object_or_404(Event, id=data['event_id'])
            event_serializer = serializers.EventSerializer(event)
            return Response(
                event_serializer.data, status=status.HTTP_201_CREATED
            )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        event = get_object_or_404(Event, id=data['event_id'])
        event_serializer = serializers.EventSerializer(event)
        return Response(
            event_serializer.data, status=status.HTTP_201_CREATED
        )

    def delete(self, request):
        try:
            event = UserActivities.objects.filter(
                event=request.data['event_id'])
            print(event)
        except UserActivities.DoesNotExist:
            return Response({'error': 'Объект не найден'},
                            status=status.HTTP_404_NOT_FOUND)

        event.delete()

        return Response({'message': 'Deleted'},
                        status=status.HTTP_204_NO_CONTENT)


class UserEventsViewSet(viewsets.ViewSet):
    """Вьюсет мероприятий пользователя"""

    def list(self, request):
        url_name = request.resolver_match.url_name
        user_activities = UserActivities.objects.filter(
            user=request.user.id).values('event')

        events_queryset = Event.objects.filter(pk__in=user_activities)
        if url_name == 'user_events-list':
            serializer = serializers.EventSerializer(
                events_queryset, many=True)

            events_data = serializer.data

            return Response(events_data)
        if url_name == 'user_completed_events-list':
            completed_events_queryset = events_queryset.filter(
                status='completed')
            serializer = serializers.EventSerializer(
                completed_events_queryset, many=True)

            events_data = serializer.data

            return Response(events_data)


# Пока сделаны только чтоб в базу данные закидывать
class UserActivitiesViewSet(viewsets.ModelViewSet):
    """Вьюсет для записей в UserActivities."""
    queryset = UserActivities.objects.all()
    serializer_class = serializers.UserActivitiesSerializer


class UserFavoritesViewSet(viewsets.ModelViewSet):
    """Вьюсет для записей в UserFavorites."""
    queryset = SelectedEvents.objects.all()
    serializer_class = serializers.UserFavoritesSerializer
