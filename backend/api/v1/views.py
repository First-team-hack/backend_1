from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from events.models import Event, Favorite

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
