from users.models import User, UserActivities, SelectedEvents
from events.models import (
    Event,
    Speaker,
    Questionnaire,
    Adress,
    Favorite,
)
from events.choices import TYPES_CHOICES, STATUS_CHOICES

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator


class SpeakerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Speaker
        fields = ('id', 'names')


class QuestionnaireSerializer(serializers.ModelSerializer):

    class Meta:
        model = Questionnaire
        fields = '__all__'


class AdresSerializer(serializers.ModelSerializer):

    type_event = serializers.ChoiceField(
        choices=TYPES_CHOICES,
        required=False,
    )
    city = serializers.CharField()

    class Meta:
        model = Adress
        fields = '__all__'


class EventShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = [
            'id',
            'topic',
            'program',
            'type_event',
            'name',
            'date',
            'time',
            'adress',
            'status',
            'speaker',
            'price'
        ]


class EventSerializer(serializers.ModelSerializer):

    type_event = serializers.ChoiceField(
        choices=TYPES_CHOICES,
        required=False,
    )
    status = serializers.ChoiceField(
        choices=STATUS_CHOICES,
        required=False,
    )

    class Meta:
        model = Event
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Favorite.objects.all(),
                fields=('user', 'recipe'),
            )
        ]


class UserSerializer(serializers.ModelSerializer):
    registeredEvents = serializers.SerializerMethodField()
    favoriteEvents = serializers.SerializerMethodField()
    recommendedEvents = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'firstName',
            'lastName',
            'email',
            'phoneNumber',
            'interest',
            'notificationByTelegram',
            'notificationByWhatsapp',
            'notificationByVk',
            'notificationByViber',
            'telegram',
            'whatsapp',
            'vk',
            'viber',
            'registeredEvents',
            'favoriteEvents',
            'recommendedEvents'
        ]

    def get_registeredEvents(self, obj):
        user_activities = UserActivities.objects.filter(
            user=self.context.user.id).values('event')
        registeredEvents = Event.objects.filter(pk__in=user_activities)
        serialized_events = EventSerializer(registeredEvents, many=True)
        return serialized_events.data

    def get_favoriteEvents(self, obj):
        user_favorites = SelectedEvents.objects.filter(
            user=self.context.user.id).values('event')
        favorite_events = Event.objects.filter(pk__in=user_favorites)
        serialized_events = EventSerializer(favorite_events, many=True)
        return serialized_events.data

    def get_recommendedEvents(self, obj):
        user_recommended = Event.objects.filter(
            themes=self.context.user.interest)
        recommended_events = Event.objects.filter(pk__in=user_recommended)
        serialized_events = EventSerializer(recommended_events, many=True)
        return serialized_events.data


class RegisteredEventSerializer(serializers.ModelSerializer):
    event = serializers.SerializerMethodField()

    class Meta:
        model = UserActivities
        fields = ['event']

    def get_event(self, obj):
        pass


class FavoritesEventSerializer(serializers.ModelSerializer):
    event = serializers.SerializerMethodField()

    class Meta:
        model = SelectedEvents
        fields = ['event']

    def get_event(self, obj):
        pass


# Пока сделаны только чтоб в базу данные закидывать
class UserActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserActivities
        fields = '__all__'


class UserFavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectedEvents
        fields = '__all__'
