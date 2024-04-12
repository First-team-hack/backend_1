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
        fields = (
            'id',
            'name',
            'type_event',
            'date',
            'speaker',
            'adress',
        )


class EventSerializer(serializers.ModelSerializer):

    type_event = serializers.ChoiceField(
        choices=TYPES_CHOICES,
        required=False,
    )
    speaker = SpeakerSerializer(many=True)
    adress = AdresSerializer()
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
